import streamlit as st

TARGET_URL = "https://www.osm.kmitl.ac.th/ranking/kmitl-sdg-matching.html"

st.set_page_config(
    page_title="KMITL SDG Matching for All",
    page_icon="🔍",
    layout="centered",
)

# ข้อความนี้ใช้ตรวจว่า Streamlit รันไฟล์ใหม่จริง
st.caption("Redirect build: 2026-07-07")

st.html(
    f"""
    <script>
        window.location.replace("{TARGET_URL}");
    </script>

    <div style="
        max-width: 680px;
        margin: 90px auto;
        padding: 32px;
        text-align: center;
        font-family: Arial, sans-serif;
    ">
        <h2>KMITL SDG Matching for All</h2>
        <p>ระบบได้ย้ายไปยังเว็บไซต์ OSM KMITL</p>
        <p>
            <a href="{TARGET_URL}" target="_self"
               style="font-size:18px;font-weight:700;">
                เปิดระบบ KMITL SDG Matching
            </a>
        </p>
    </div>
    """,
    unsafe_allow_javascript=True,
)

st.stop()
