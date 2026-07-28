import streamlit as st


# ==========================================================
# PALET WARNA (DARK & SIMPLE)
# ==========================================================

PRIMARY = "#2F2FE4"       # indigo lembut untuk aksen
SUCCESS = "#22C55E"
WARNING = "#EAB308"
DANGER = "#EF4444"

BG = "#0E1117"            # background utama
SIDEBAR_BG = "#12151C"
CARD_BG = "#161A22"
BORDER = "#262B36"
TEXT = "#E5E7EB"
TEXT_MUTED = "#9CA3AF"


# ==========================================================
# CSS GLOBAL
# ==========================================================

def load_css():

    st.markdown(
        f"""
        <style>

        /* ---------- Base ---------- */
        .stApp {{
            background: {BG};
            color: {TEXT};
        }}

        html, body, [class*="css"] {{
            font-family: "Segoe UI", "Inter", sans-serif;
            color: {TEXT};
        }}

        #MainMenu, footer {{
            visibility: hidden;
        }}

        header[data-testid="stHeader"] {{
            background: transparent;
        }}

        .block-container {{
            padding-top: 2rem;
            padding-bottom: 3rem;
        }}

        /* ---------- Sidebar ---------- */
        section[data-testid="stSidebar"] {{
            background: {SIDEBAR_BG};
            border-right: 1px solid {BORDER};
        }}

        section[data-testid="stSidebar"] * {{
            color: {TEXT} !important;
        }}

        section[data-testid="stSidebar"] div[role="radiogroup"] label {{
            border-radius: 8px;
            padding: 6px 10px;
        }}

        section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {{
            background: {CARD_BG};
        }}

        section[data-testid="stSidebar"] hr {{
            border-color: {BORDER};
        }}

        section[data-testid="stSidebar"] button {{
            background: transparent !important;
            border: 1px solid {BORDER} !important;
            color: {TEXT} !important;
        }}

        section[data-testid="stSidebar"] button:hover {{
            border-color: {PRIMARY} !important;
            color: {PRIMARY} !important;
        }}

        /* ---------- Headings & text ---------- */
        h1, h2, h3, h4 {{
            color: {TEXT};
            font-weight: 600;
        }}

        p, span, label, li {{
            color: {TEXT};
        }}

        /* ---------- Buttons (main area) ---------- */
        div[data-testid="stAppViewContainer"] .stButton button {{
            background: {PRIMARY};
            color: #0E1117;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            font-weight: 600;
        }}

        div[data-testid="stAppViewContainer"] .stButton button:hover {{
            opacity: 0.85;
        }}

        /* ---------- Inputs ---------- */
        .stTextInput input,
        .stNumberInput input,
        .stSelectbox div[data-baseweb="select"] > div,
        .stTextArea textarea {{
            background: {CARD_BG} !important;
            color: {TEXT} !important;
            border: 1px solid {BORDER} !important;
            border-radius: 8px !important;
        }}

        /* ---------- Tabs ---------- */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 4px;
            border-bottom: 1px solid {BORDER};
        }}

        .stTabs [data-baseweb="tab"] {{
            background: transparent;
            border-radius: 6px 6px 0 0;
            padding: 8px 16px;
            font-weight: 600;
            color: {TEXT_MUTED};
        }}

        .stTabs [aria-selected="true"] {{
            color: {PRIMARY} !important;
            border-bottom: 2px solid {PRIMARY};
        }}

        /* ---------- Metric cards ---------- */
        div[data-testid="stMetric"] {{
            background: {CARD_BG};
            border: 1px solid {BORDER};
            border-radius: 10px;
            padding: 0.9rem 1rem;
        }}

        div[data-testid="stMetricLabel"] {{
            color: {TEXT_MUTED} !important;
        }}

        /* ---------- Dataframe / table ---------- */
        div[data-testid="stDataFrame"] {{
            border-radius: 10px;
            overflow: hidden;
            border: 1px solid {BORDER};
        }}

        /* ---------- Alerts ---------- */
        div[data-testid="stAlert"] {{
            border-radius: 10px;
        }}

        /* ---------- Progress bar ---------- */
        div[data-testid="stProgressBarTrack"] {{
            background: {BORDER} !important;
        }}

        div[data-testid="stProgressBarTrack"] > div {{
            background: {PRIMARY} !important;
        }}

        /* ---------- File uploader ---------- */
        section[data-testid="stFileUploaderDropzone"] {{
            background: {CARD_BG};
            border: 1px dashed {BORDER};
            border-radius: 10px;
        }}

        /* ---------- Divider ---------- */
        hr {{
            border-color: {BORDER};
            margin: 1.1rem 0;
        }}

        /* ---------- Custom card ---------- */
        .app-card {{
            background: {CARD_BG};
            border: 1px solid {BORDER};
            border-radius: 12px;
            padding: 1.2rem 1.4rem;
            margin-bottom: 1rem;
        }}

        .app-badge {{
            display: inline-block;
            padding: 3px 10px;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: 700;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# KOMPONEN BANTUAN
# ==========================================================

def page_header(title, subtitle=None):
    """Header halaman: judul + subjudul, tanpa ikon."""

    st.markdown(
        f"""
        <div style="font-size:1.4rem;font-weight:700;color:{TEXT};margin-bottom:0.2rem;">{title}</div>
        {f'<div style="color:{TEXT_MUTED};font-size:0.9rem;margin-bottom:0.8rem;">{subtitle}</div>' if subtitle else ''}
        <div style="height:1px;background:{BORDER};margin:0.8rem 0 1.2rem 0;"></div>
        """,
        unsafe_allow_html=True
    )


def badge(text, color=SUCCESS):
    return f'<span class="app-badge" style="background:{color}22;color:{color};">{text}</span>'


def card_open():
    st.markdown('<div class="app-card">', unsafe_allow_html=True)


def card_close():
    st.markdown('</div>', unsafe_allow_html=True)
