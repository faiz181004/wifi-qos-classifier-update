import streamlit as st
from database import create_tables
from auth import (
    init_session,
    login_user,
    register_user,
    logout,
    is_login,
    is_admin
)

from model import (
    load_dataset,
    train_model,
    load_model,
    predict
)

from modules import (
    admin_dashboard,
    admin_users,
    admin_data,
    admin_input,
    user_home,
    user_input,
    user_hasil,
    export,
    style
)

# ==========================
# CONFIG
# ==========================

st.set_page_config(
    page_title="WiFi QoS Classifier",
    page_icon="📶",
    layout="wide",
    initial_sidebar_state="expanded"
)

style.load_css()

# ==========================
# DATABASE
# ==========================

create_tables()

# ==========================
# SESSION
# ==========================

init_session()

# ==========================
# LOAD DATASET
# ==========================

DATASET_PATH = "dataset_wifi.csv"

df = load_dataset(DATASET_PATH)

hasil_model = train_model(df)

model = load_model()

# ==========================
# LOGIN
# ==========================

if not is_login():

    col_kiri, col_tengah, col_kanan = st.columns(
        [1, 1.3, 1]
    )

    with col_tengah:


        st.markdown(
            f"""
            <div style="text-align:center;margin-bottom:1rem;">
                <div style="font-size:1.4rem;font-weight:700;">WiFi QoS Classifier</div>
                <div style="color:{style.TEXT_MUTED};font-size:0.9rem;margin-top:0.3rem;">
                    Sistem klasifikasi kualitas layanan WiFi
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        tab_login, tab_register = st.tabs([
            "Login",
            "Register"
        ])

        # ======================
        # LOGIN
        # ======================

        with tab_login:

            email = st.text_input(
                "Email"
            )

            password = st.text_input(
                "Password",
                type="password"
            )

            if st.button(
                "Masuk",
                use_container_width=True
            ):

                if login_user(
                    email,
                    password
                ):

                    st.success(
                        "Login berhasil"
                    )

                    st.rerun()

                else:

                    st.error(
                        "Email atau Password salah"
                    )

        # ======================
        # REGISTER
        # ======================

        with tab_register:

            nama = st.text_input(
                "Nama Lengkap"
            )

            email = st.text_input(
                "Email",
                key="reg_email"
            )

            password = st.text_input(
                "Password",
                type="password",
                key="reg_pass"
            )

            konfirmasi = st.text_input(
                "Konfirmasi Password",
                type="password"
            )

            if st.button(
                "Daftar Sekarang",
                use_container_width=True
            ):

                if password != konfirmasi:

                    st.error(
                        "Password tidak sama"
                    )

                else:

                    sukses, pesan = register_user(
                        nama,
                        email,
                        password
                    )

                    if sukses:

                        st.success(
                            pesan
                        )

                    else:

                        st.error(
                            pesan
                        )


    st.stop()

# ==========================
# SIDEBAR
# ==========================

nama_user = st.session_state["nama"] or "Pengguna"
inisial = nama_user.strip()[0].upper() if nama_user.strip() else "U"
role_user = st.session_state["role"].upper()

st.sidebar.markdown(
    f"""
    <div style="text-align:center;padding:0.4rem 0 1rem 0;">
        <div style="font-size:1.3rem;font-weight:700;">WiFi QoS</div>
        <div style="
            width:48px;height:48px;border-radius:50%;
            background:{style.CARD_BG};
            border:1px solid {style.BORDER};
            display:flex;align-items:center;justify-content:center;
            font-size:1.2rem;font-weight:700;
            margin:0.8rem auto 0.4rem auto;
            color:{style.PRIMARY};
        ">{inisial}</div>
        <div style="font-weight:600;">{nama_user}</div>
        <div style="
            display:inline-block;margin-top:4px;
            background:{style.CARD_BG};
            border:1px solid {style.BORDER};
            padding:2px 10px;border-radius:6px;
            font-size:0.72rem;letter-spacing:0.4px;font-weight:700;
            color:{style.TEXT_MUTED};
        ">{role_user}</div>
    </div>
    """,
    unsafe_allow_html=True
)

if is_admin():

    menu_map = {
        "Dashboard": "Dashboard",
        "Input Data": "Input Data Admin",
        "User": "User",
        "Data User": "Data User",
        "Ekspor": "Ekspor"
    }

else:

    menu_map = {
        "Beranda": "Beranda",
        "Input Data": "Input Data",
        "Hasil Saya": "Hasil Saya"
    }

pilihan_menu = st.sidebar.radio(
    "Menu",
    list(menu_map.keys())
)

halaman = menu_map[pilihan_menu]

st.sidebar.divider()

if st.sidebar.button(
    "Logout",
    use_container_width=True
):

    logout()

# ==========================
# ROUTING
# ==========================

if halaman == "Dashboard":

    admin_dashboard.show(
        hasil_model
    )

elif halaman == "User":

    admin_users.show()

elif halaman == "Input Data Admin":

    admin_input.show(
        model,
        predict
    )

elif halaman == "Data User":

    admin_data.show()

elif halaman == "Ekspor":

    export.show(
        hasil_model
    )

elif halaman == "Beranda":

    user_home.show(
        df,
        hasil_model,
        "label_kelas",
        [
            "Buruk",
            "Sedang",
            "Baik",
            "Sangat Baik"
        ],
        nama_user
    )

elif halaman == "Input Data":

    user_input.show(
        model,
        predict
    )

elif halaman == "Hasil Saya":

    user_hasil.show()

