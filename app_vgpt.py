import streamlit as st
import time
from matcher import match_text
import os

# ===== Page Configuration =====

st.set_page_config(page_title="KMITL SDG Matching for All", layout="wide", initial_sidebar_state="collapsed")

import time
now = time.time()
from datetime import datetime, timezone, timedelta
thai_time = datetime.fromtimestamp(now, timezone(timedelta(hours=7)))

# ===== SDG Names for Display =====

sdg_names = {str(i): name for i, name in enumerate([
    "No Poverty", "Zero Hunger", "Good Health and Well-being", "Quality Education", "Gender Equality",
    "Clean Water and Sanitation", "Affordable and Clean Energy", "Decent Work and Economic Growth",
    "Industry, Innovation and Infrastructure", "Reduced Inequality", "Sustainable Cities and Communities",
    "Responsible Consumption and Production", "Climate Action", "Life Below Water", "Life on Land",
    "Peace, Justice and Strong Institutions", "Partnerships for the Goals"
], start=1)}

# ===== CSS Styling (Responsive) =====

st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
    color: #333;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.flex-header {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    margin-top: 30px;
    margin-bottom: 20px;
    flex-wrap: wrap;
}
.flex-header img {
    width: clamp(28px, 5vw, 48px);
    height: auto;
}
.responsive-title {
    font-size: clamp(28px, 6vw, 48px);
    font-weight: bold;
    color: #f26f21;
    text-align: center;
}

.subtitle {
    text-align: center;
    font-size: clamp(14px, 2vw, 20px);
    margin-bottom: 36px;
}

.stTextArea label {
    font-size: clamp(20px, 5vw, 36px) !important;
    font-weight: 700;
}
.stTextArea textarea {
    font-size: clamp(14px, 2.5vw, 18px) !important;
    padding: 1em;
}

.stButton > button {
    background-color: #f26f21;
    color: white;
    font-size: clamp(18px, 4vw, 28px);
    font-weight: bold;
    padding: 0.4em 1em;
    border-radius: 10px;
}
.stButton > button:hover {
    background-color: #d95400;
}

.sdg-result {
    font-size: clamp(16px, 3vw, 22px);
    color: #444;
    font-weight: 600;
    line-height: 1.4;
}

.footer {
    text-align: center;
    margin-top: 30px;
    font-size: clamp(12px, 2vw, 16px);
    color: #444;
    line-height: 1.8;
}
.footer em {
    font-size: clamp(12px, 2vw, 16px);
}
.footer small {
    font-size: clamp(10px, 1.5vw, 14px);
    color: #888;
}
</style>
""", unsafe_allow_html=True)

# ===== Header =====

st.markdown("""
<div class="flex-header">
    <div class="responsive-title">KMITL SDG Matching for All</div>
    <img src="https://raw.githubusercontent.com/Sabas446/KMITL-SDG-Matching/main/osm_logo.png">
</div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class='subtitle'>
        🔍 เช็กข้อความของคุณว่าสอดคล้องกับเป้าหมายการพัฒนาที่ยั่งยืน (SDGs) ข้อใดบ้าง<br>
        รองรับทั้ง <strong>ภาษาไทย</strong> และ <strong>ภาษาอังกฤษ</strong><br><br>
    </div>
""", unsafe_allow_html=True)
st.markdown("---")

# ===== Input and Submit =====

text_input = st.text_area("📥 กรุณาใส่ข้อความที่ต้องการตรวจสอบ:", height=300)
if st.button("🔍 วิเคราะห์"):
    if text_input.strip() == "":
        st.warning("⚠️ กรุณาใส่ข้อความก่อนกด วิเคราะห์")
    else:
        matched_sdgs = match_text(text_input)
        if matched_sdgs:
            matched_sdgs = sorted(matched_sdgs, key=lambda x: int(x))
            st.success(f"✅ พบ {len(matched_sdgs)} เป้าหมายที่เกี่ยวข้อง")
            for sdg in matched_sdgs:
                name = sdg_names.get(sdg, 'Unknown SDG')
                icon_path = f"icons/{sdg}.png"
                default_icon = "icons/default.png"
                used_icon = icon_path if os.path.exists(icon_path) else default_icon if os.path.exists(default_icon) else None
                if used_icon:
                    cols = st.columns([0.13, 0.87])
                    with cols[0]:
                        st.image(used_icon, width=50)
                    with cols[1]:
                        st.markdown(f"<div style='display:flex; align-items:center; height:50px;'><span class='sdg-result'>SDG {sdg}: {name}</span></div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<span class='sdg-result'>SDG {sdg}: {name}</span>", unsafe_allow_html=True)

            base_hashtags = "#KMITL #สจล #พระจอมเกล้าลาดกระบัง"
            sdg_hashtags = ' '.join([f"#SDG{sdg}" for sdg in matched_sdgs])
            full_hashtags = base_hashtags + "\n" + sdg_hashtags

            st.markdown("### ✨ สรุปการวิเคราะห์ (Hashtag)")
            st.code(full_hashtags, language=None)        

        else:
            st.info("ไม่พบคำที่ตรงกับ SDGs ในข้อความนี้")


# ===== Footer =====

st.markdown("---")
st.markdown(f"""
    <div class="footer">
        <em>
            ระบบนี้พัฒนาภายใต้แนวคิด Routine to Research (R2R) โดยนักวิเคราะห์นโยบายและแผน สจล.<br>
            มุ่งสร้างเครื่องมือสำหรับวิเคราะห์ข้อความให้สอดคล้องกับ SDGs อย่างแม่นยำ<br>
            ครอบคลุมเฉพาะเป้าหมายที่เกี่ยวข้อง เพื่อสนับสนุนการสื่อสารข้อมูลความยั่งยืนของสถาบัน
        </em><br>
        <small>© 2025 Office of Strategy Management KMITL</small>
    </div>
""", unsafe_allow_html=True)
