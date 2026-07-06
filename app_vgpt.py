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
    <!doctype html>
    <html lang="th">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="refresh" content="0; url={TARGET_URL}">
        <script>
            window.location.replace("{TARGET_URL}");
        </script>
    </head>
    <body>
        <p>
            ระบบได้ย้ายไปยัง
            <a href="{TARGET_URL}">เว็บไซต์ OSM KMITL</a>
        </p>
    </body>
    </html>
    """,
    unsafe_allow_javascript=True,
)

st.stop()
