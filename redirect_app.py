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
            max-width: 760px;
            padding-top: 6rem;
        }

        .redirect-card {
            padding: 42px 34px;
            text-align: center;
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-top: 5px solid #f97316;
            border-radius: 18px;
            box-shadow: 0 14px 35px rgba(0, 0, 0, 0.08);
            font-family: Arial, sans-serif;
        }

        .redirect-title {
            margin: 0 0 14px;
            color: #f97316;
            font-size: 34px;
            font-weight: 800;
        }

        .redirect-message {
            margin: 0 0 8px;
            color: #111827;
            font-size: 18px;
            font-weight: 700;
        }

        .redirect-detail {
            margin: 0 0 28px;
            color: #6b7280;
            font-size: 14px;
        }

        .redirect-button {
            display: inline-block;
            padding: 14px 26px;
            color: #ffffff !important;
            background: #f97316;
            border-radius: 10px;
            font-size: 17px;
            font-weight: 700;
            text-decoration: none !important;
            box-shadow: 0 8px 18px rgba(249, 115, 22, 0.25);
        }

        .redirect-button:hover {
            background: #ea580c;
        }

        .backup-link {
            margin-top: 24px;
            color: #6b7280;
            font-size: 13px;
        }

        .backup-link a {
            color: #2563eb;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
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

        <a
            class="redirect-button"
            href="{TARGET_URL}"
            target="_top"
        >
            🔍 เปิดระบบ KMITL SDG Matching
        </a>

        <div class="backup-link">
            หากปุ่มไม่เปลี่ยนหน้า
            <a href="{TARGET_URL}" target="_blank">
                เปิดระบบในแท็บใหม่
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.stop()
