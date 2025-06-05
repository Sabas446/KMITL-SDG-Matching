import streamlit as st
from matcher import match_text
from google_sheet_utils import log_action_to_sheet, get_stats_from_logs
import os
import time

# ===== Logo with st.image() =====
st.markdown("""
<style>
.header-flex {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    margin-top: 10px;
    flex-wrap: wrap;
}
.header-flex img {
    max-width: 50px;
    height: auto;
}
@media (max-width: 768px) {
    .header-flex {
        flex-direction: column;
        gap: 10px;
    }
}
</style>

<div class="header-flex">
    <div class='main-title'>KMITL SDG Matching for All</div>
    <img src='https://raw.githubusercontent.com/Sabas446/KMITL-SDG-Matching/main/osm_logo.png'>
</div>
""", unsafe_allow_html=True)

params = st.query_params
user_agent = st.request.headers.get("user-agent", "").lower()

# หากเป็นการปลุกจาก bot หรือ uptime หรือพารามิเตอร์ที่ขึ้นต้นว่า wake ให้หยุดทันที
if any(k.startswith("wake") for k in params) or "uptimerobot" in user_agent or "bot" in user_agent:
    st.stop()

now = time.time()
if "last_visit_logged" not in st.session_state or now - st.session_state["last_visit_logged"] > 1800:  # 30 นาที
    log_action_to_sheet("visit", user_agent=user_agent, query=params)
    st.session_state["last_visit_logged"] = now

# ===== SDG Names for Display =====
sdg_names = {str(i): name for i, name in enumerate([
    "No Poverty", "Zero Hunger", "Good Health and Well-being", "Quality Education", "Gender Equality",
    "Clean Water and Sanitation", "Affordable and Clean Energy", "Decent Work and Economic Growth",
    "Industry, Innovation and Infrastructure", "Reduced Inequality", "Sustainable Cities and Communities",
    "Responsible Consumption and Production", "Climate Action", "Life Below Water", "Life on Land",
    "Peace, Justice and Strong Institutions", "Partnerships for the Goals"
], start=1)}

# ===== CSS Styling =====
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
            font-size: 14.5px;
            color: #333333;
        }
        .main-title {
            text-align: center;
            color: #f26f21;
            font-size: 48px;
            font-weight: bold;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            margin-bottom: 36px;
        }
        .stTextArea label {
            font-size: 48px !important;
            font-weight: 700;
        }
        .stTextArea textarea {
            font-size: 18px !important;
            padding: 1em;
        }
        .stButton > button {
            background-color: #f26f21;
            color: white;
            font-size: 36px;
            font-weight: bold;
            padding: 0.3em 1em;
            height: 45px;
            min-width: 120px;
            width: fit-content;
            border-radius: 10px;
        }
        .stButton > button:hover {
            background-color: #d95400;
        }
        .stButton > button:active {
            background-color: #ba4c0a !important;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# ===== Header =====
st.markdown("""
    <div class='subtitle'>
        🔍 เช็กข้อความของคุณว่าสอดคล้องกับเป้าหมายการพัฒนาที่ยั่งยืน (SDGs) ข้อใด้บ้าง<br>
        รองรับทั้ง <strong>ภาษาไทย</strong> และ <strong>ภาษาอังกฤษ</strong><br><br>
    </div>
""", unsafe_allow_html=True)
st.markdown("---")

# ===== Input and Submit =====
text_input = st.text_area("📥 กรุณาใส่ข้อความที่ต้องการตรวจสอบ:", height=300)
if st.button("🔍 วิเคราะร้อง"):
    if text_input.strip() == "":
        st.warning("⚠️ กรุณาใส่ข้อความก่อนกด วิเคราะร้อง")
    else:
        log_action_to_sheet("check", user_agent=user_agent, query=params)
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
                        st.markdown(f"<div style='display:flex; align-items:center; height:50px;'><span style='font-size:22px; color:#444; font-weight:600; line-height:1;'>SDG {sdg}: {name}</span></div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<span style='font-size:22px; color:#444; font-weight:600;'>SDG {sdg}: {name}</span>", unsafe_allow_html=True)
            base_hashtags = "#KMITL #สจล #พระจอมเกล้าลาดกระบัง"
            sdg_hashtags = ' '.join([f"#SDG{sdg}" for sdg in matched_sdgs])
            full_hashtags = base_hashtags + "\n" + sdg_hashtags
            st.markdown("### ✨ สรุปการวิเคราะร้อง (Hashtag)")
            st.code(full_hashtags, language=None)
        else:
            st.info("ไม่พบคำที่ตรงกับ SDGs ในข้อความนี้")

total_visits, total_checks, month_visits, month_checks = get_stats_from_logs()

# ===== Footer =====
st.markdown("---")
st.markdown(f"""
    <div style='text-align:center; margin-top: 30px; font-size: 16px; color: #444; line-height: 1.8;'>
        <em>
            ระบบนี้พัฒนาภายใต้แนวคิด Routine to Research (R2R) โดยนักวิเคราะนโยบายและแผน สจล.<br>
            มุ่งสร้างเครื่อมือสำหรับวิเคราะข้อความให้สอดคล้องกับ SDGs อย่างแม่นยำ<br>
            ครอบคุมเฉพะเป้าหมายที่เกี่ยวข้อง เพื่อสนับสนุนการสื่อสารข้อมูลความยั่งยืนของสถาบัน
        </em>
        <br><br>
        👥 <strong>ผู้เข้าใช้งานรวม:</strong> {total_visits} ครั้ง |
        📊 <strong>ข้อความที่วิเคราะรวม:</strong> {total_checks} ข้อความ<br>
        📅 <strong>เดือนนี้:</strong> 👥 {month_visits} ครั้ง | 📊 {month_checks} ข้อความ
        <br><br>
        <span style='font-size: 14px; color: #888;'>© 2025 Office of Strategy Management KMITL</span>
    </div>
""")
