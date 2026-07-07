import streamlit as st
from textwrap import dedent

TARGET_URL = "https://www.osm.kmitl.ac.th/ranking/kmitl-sdg-matching.html"

st.set_page_config(
    page_title="KMITL SDG Matching for All",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.html(
    dedent(
        f"""
        <style>
            [data-testid="stHeader"],
            [data-testid="stSidebar"],
            footer,
            #MainMenu {{
                display: none !important;
            }}

            .stMainBlockContainer {{
                max-width: 760px;
                padding-top: 80px;
            }}

            .redirect-card {{
                max-width: 680px;
                margin: 0 auto;
                padding: 44px 36px;
                text-align: center;
                font-family: Arial, sans-serif;
                background: white;
                border: 1px solid #e5e7eb;
                border-top: 5px solid #f97316;
                border-radius: 18px;
                box-shadow: 0 14px 35px rgba(0, 0, 0, 0.08);
            }}

            .redirect-title {{
                margin-bottom: 14px;
                color: #f97316;
                font-size: 34px;
                font-weight: 800;
            }}

            .redirect-message {{
                margin-bottom: 8px;
                color: #111827;
                font-size: 19px;
                font-weight: 700;
            }}

            .redirect-detail {{
                margin-bottom: 28px;
                color: #6b7280;
                font-size: 15px;
            }}

            .redirect-button {{
                display: inline-block;
                padding: 14px 28px;
                color: white !important;
                background: #f97316;
                border-radius: 10px;
                font-size: 17px;
                font-weight: 700;
                text-decoration: none !important;
                box-shadow: 0 8px 18px rgba(249, 115, 22, 0.25);
            }}

            .redirect-button:hover {{
                background: #ea580c;
            }}

            .redirect-note {{
                margin-top: 24px;
                color: #9ca3af;
                font-size: 12px;
            }}
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

            <a
                class="redirect-button"
                href="{TARGET_URL}"
                target="_self"
            >
                🔍 เปิดระบบ KMITL SDG Matching
            </a>

            <div class="redirect-note">
                KMITL SDG Matching for All V2
            </div>
        </div>
        """
    ).strip()
)

st.stop()
