import streamlit as st

TARGET_URL = "https://www.osm.kmitl.ac.th/ranking/kmitl-sdg-matching.html"

st.set_page_config(
    page_title="KMITL SDG Matching for All",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ซ่อนเมนูและส่วนประกอบของ Streamlit ที่ไม่จำเป็น
st.markdown(
    """
    <style>
        [data-testid="stHeader"],
        [data-testid="stSidebar"],
        footer,
        #MainMenu {
            display: none !important;
        }

        .block-container {
            max-width: 760px;
            padding-top: 7rem;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-top: 5px solid #f97316 !important;
            border-radius: 18px !important;
            padding: 24px !important;
            box-shadow: 0 14px 35px rgba(0, 0, 0, 0.08);
        }

        div[data-testid="stLinkButton"] a {
            background-color: #f97316 !important;
            color: white !important;
            border: none !important;
            min-height: 52px;
            font-size: 17px;
            font-weight: 700;
            border-radius: 10px;
        }

        div[data-testid="stLinkButton"] a:hover {
            background-color: #ea580c !important;
            color: white !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.container(border=True):
    st.markdown(
        "<h1 style='text-align:center; color:#f97316;'>"
        "KMITL SDG Matching for All"
        "</h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<h3 style='text-align:center;'>"
        "ระบบได้ย้ายไปยังเว็บไซต์ OSM KMITL"
        "</h3>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<p style='text-align:center; color:#6b7280;'>"
        "กรุณากดปุ่มด้านล่างเพื่อเปิดระบบเวอร์ชันล่าสุด"
        "</p>",
        unsafe_allow_html=True,
    )

    st.link_button(
        "🔍 เปิดระบบ KMITL SDG Matching",
        TARGET_URL,
        type="primary",
        use_container_width=True,
    )

    st.markdown(
        "<p style='text-align:center; color:#9ca3af; font-size:12px;'>"
        "KMITL SDG Matching for All V2"
        "</p>",
        unsafe_allow_html=True,
    )

st.stop()
