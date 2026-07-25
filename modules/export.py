import streamlit as st
import pandas as pd

from database import get_connection
from modules import style

def warna_hasil(val):

    if val == "Buruk":
        return "background-color:#dc3545; color:white;"

    elif val == "Sedang":
        return "background-color:#FFD966; color:black;"

    elif val == "Baik":
        return "background-color:#90EE90; color:black;"

    elif val == "Sangat Baik":
        return "background-color:#1E7E34; color:white;"

    return ""

def show(hasil_model):

    style.page_header(
        "Ekspor Laporan",
        "Unduh data klasifikasi dan lihat evaluasi model"
    )

    conn = get_connection()

    query = """
        SELECT
        hasil.id,
        users.nama,
        users.email,
        hasil.download_speed,
        hasil.upload_speed,
        hasil.latency,
        hasil.packet_loss,
        hasil.skor_keluhan,
        hasil.label_kelas,
        hasil.hasil,
        hasil.tanggal
    FROM hasil
    JOIN users
    ON hasil.user_id = users.id
    ORDER BY hasil.id DESC
    """

    df = pd.read_sql(query, conn)

    conn.close()

    if len(df) == 0:

        st.warning("Belum ada data.")

        return

    styled_df = (
    df.style
    .format({
        "download_speed": "{:.2f}",
        "upload_speed": "{:.2f}",
        "latency": "{:.2f}",
        "packet_loss": "{:.2f}",
        "skor_keluhan": "{:.2f}",
    })
    .map(warna_hasil, subset=["hasil"])
    .map(warna_hasil, subset=["label_kelas"])
    )

    st.dataframe(
        styled_df,
        use_container_width=True
    )

    csv = df.to_csv(index=False).encode()

    st.download_button(
        "Download CSV",
        csv,
        "laporan.csv",
        "text/csv"
    )

    st.divider()

    st.subheader("Evaluasi Model")

    m1, m2, m3, m4 = st.columns(4)

    m1.metric(
        "Akurasi",
        f"{hasil_model['akurasi']*100:.2f}%"
    )

    m2.metric(
        "Precision",
        f"{hasil_model['presisi']*100:.2f}%"
    )

    m3.metric(
        "Recall",
        f"{hasil_model['recall']*100:.2f}%"
    )

    m4.metric(
        "F1 Score",
        f"{hasil_model['f1']*100:.2f}%"
    )
