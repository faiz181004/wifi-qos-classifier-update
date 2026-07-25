import streamlit as st
from modules import style

def show(df_bersih, hasil_model, LABEL, URUTAN_KELAS, nama_user):

    style.page_header(
        "Beranda",
        "Media Elektronik Kerinci — Layanan Internet WiFi"
    )

    # ==========================================================
    # HALO USER
    # ==========================================================

    st.markdown(
        f"""
    ## 👋 Halo, **{nama_user}**

    Selamat datang di aplikasi klasifikasi kualitas layanan WiFi.
    Semoga aktivitas Anda hari ini berjalan lancar.
    """
    )

    st.divider()

    # ==========================================================
    # TENTANG APLIKASI
    # ==========================================================

    st.info("""
**Tentang Aplikasi**

Aplikasi ini digunakan untuk mengklasifikasikan kualitas layanan WiFi
berdasarkan hasil pengukuran jaringan dan keluhan pengguna.

Parameter yang digunakan:

- Download Speed
- Upload Speed
- Latency
- Packet Loss
- Keluhan Pengguna

Hasil klasifikasi terdiri dari:

- Sangat Baik
- Baik
- Sedang
- Buruk
""")

    st.divider()

    # ==========================================================
    # CARA MENGGUNAKAN
    # ==========================================================

    st.subheader("Cara Menggunakan")

    st.markdown("""
1. Pilih menu **Input Data**.
2. Masukkan hasil **Speedtest** dan data keluhan.
3. Klik **Jalankan Klasifikasi**.
4. Lihat hasil pada menu **Hasil Saya**.
""")