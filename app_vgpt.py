import streamlit as st

TARGET_URL = (
    "https://www.osm.kmitl.ac.th/"
    "ranking/kmitl-sdg-matching.html"
)

st.set_page_config(
    page_title="KMITL SDG Matching for All",
    page_icon="🔍",
    layout="centered",
)

st.html(
    f"""
    <script>
        window.location.replace("{TARGET_URL}");
    </script>

    <div style="
        max-width: 680px;
        margin: 80px auto;
        padding: 32px;
        text-align: center;
        font-family: Arial, sans-serif;
    ">
        <h2>KMITL SDG Matching for All</h2>
        <p>ระบบได้ย้ายไปยังเว็บไซต์ OSM KMITL</p>
        <p>
            <a href="{TARGET_URL}">
                คลิกที่นี่หากระบบไม่เปลี่ยนหน้าอัตโนมัติ
            </a>
        </p>
    </div>
    """,
    unsafe_allow_javascript=True,
)

st.stop()
