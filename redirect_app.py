import streamlit as st

# หน้าเว็บไซต์ OSM ที่ต้องการส่งผู้ใช้ไป
TARGET_URL = "https://www.osm.kmitl.ac.th/ranking/kmitl-sdg-matching.html"

st.set_page_config(
    page_title="KMITL SDG Matching for All",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ซ่อนองค์ประกอบของ Streamlit ที่ไม่จำเป็น
st.markdown(
    """
    <style>
        [data-testid="stHeader"] {
            display: none;
        }

        [data-testid="stSidebar"] {
            display: none;
        }

        footer {
            display: none;
        }

        .block-container {
            max-width: 760px;
            padding-top: 5rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Redirect ออกจากกรอบ Streamlit ไปยังหน้าหลักของ Browser
st.html(
    f"""
    <script>
        const targetUrl = "{TARGET_URL}";

        try {{
            if (window.top) {{
                window.top.location.replace(targetUrl);
            }} else {{
                window.location.replace(targetUrl);
            }}
        }} catch (error) {{
            window.location.href = targetUrl;
        }}
    </script>

    <div style="
        max-width: 680px;
        margin: 40px auto;
        padding: 36px;
        text-align: center;
        font-family: Arial, sans-serif;
        border: 1px solid #e5e7eb;
        border-top: 5px solid #f97316;
        border-radius: 16px;
        background: #ffffff;
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
    ">
        <h1 style="
            margin: 0 0 12px 0;
            color: #f97316;
            font-size: 32px;
        ">
            KMITL SDG Matching for All
        </h1>

        <p style="
            margin: 0 0 8px 0;
            font-size: 17px;
            font-weight: 700;
            color: #111827;
        ">
            ระบบได้ย้ายไปยังเว็บไซต์ OSM KMITL
        </p>

        <p style="
            margin: 0 0 24px 0;
            color: #6b7280;
            font-size: 14px;
        ">
            กำลังนำท่านไปยังระบบเวอร์ชันล่าสุด
        </p>

        <a
            href="{TARGET_URL}"
            target="_top"
            style="
                display: inline-block;
                padding: 13px 24px;
                border-radius: 10px;
                background: #f97316;
                color: #ffffff;
                font-size: 16px;
                font-weight: 700;
                text-decoration: none;
            "
        >
            เปิดระบบ KMITL SDG Matching
        </a>

        <p style="
            margin-top: 24px;
            color: #9ca3af;
            font-size: 12px;
        ">
            Redirect build: 2026-07-07
        </p>
    </div>
    """,
    unsafe_allow_javascript=True,
)

st.stop()
