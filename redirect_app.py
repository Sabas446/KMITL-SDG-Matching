import streamlit as st

TARGET_URL = "https://www.osm.kmitl.ac.th/ranking/kmitl-sdg-matching.html"

st.set_page_config(
    page_title="KMITL SDG Matching for All",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="collapsed",
)

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
            max-width: 680px;
            padding-top: 6rem;
        }

        .redirect-card {
            padding: 42px 36px 24px;
            text-align: center;
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-top: 5px solid #f97316;
            border-radius: 18px 18px 0 0;
            box-shadow: 0 14px 35px rgba(0, 0, 0, 0.08);
        }

        .redirect-title {
            color: #f97316;
            font-size: 34px;
            font-weight: 800;
            margin-bottom: 14px;
        }

        .redirect-message {
            color: #111827;
            font-size: 19px;
            font-weight: 700;
            margin-bottom: 8px;
        }

        .redirect-detail {
            color: #6b7280;
            font-size: 14px;
            margin-bottom: 8px;
        }

        /* ปรับปุ่ม Link Button ให้เป็นสีส้ม */
        div[data-testid="stLinkButton"] {
            background: #ffffff;
            padding: 2px 36px 32px;
            border-left: 1px solid #e5e7eb;
            border-right: 1px solid #e5e7eb;
            border-bottom: 1px solid #e5e7eb;
            border-radius: 0 0 18px 18px;
            box-shadow: 0 14px 35px rgba(0, 0, 0, 0.08);
        }

        div[data-testid="stLinkButton"] a {
            background: #f97316 !important;
            color: #ffffff !important;
            border: none !important;
            min-height: 52px;
            font-size: 17px;
            font-weight: 700;
            border-radius: 10px;
        }

        div[data-testid="stLinkButton"] a:hover {
            background: #ea580c !important;
            color: #ffffff !important;
        }

        .version-note {
            text-align: center;
            color: #9ca3af;
            font-size: 12px;
            margin-top: 18px;
        }
    </style>

    <div class="redirect-card">
        <div class="redirect-title">
            KMITL SDG Matching for All
        </div>

        <div class="redirect-message">
            ระบบได้ย้ายไปยังเว็บไซต์ OSM KMITL
        </div>

        <div class="redirect-detail">
            กรุณากดปุ่มด้านล่างเพื่อเปิดระบบเวอร์ชันล่าสุด
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.link_button(
    "🔍 เปิดระบบ KMITL SDG Matching",
    TARGET_URL,
    type="primary",
    use_container_width=True,
)

st.markdown(
    '<div class="version-note">KMITL SDG Matching for All V2</div>',
    unsafe_allow_html=True,
)

st.stop()
