
import streamlit as st
from matcher import match_text
import os

# ===== Wake check =====
params = st.experimental_get_query_params()
if "wake" in params:
    st.write("✅ App is awake.")
    st.stop()

# ===== Page Configuration =====
st.set_page_config(
    page_title="KMITL SDG Matching for All",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===== SDG Names for Display =====
sdg_names = {
    '1': 'No Poverty',
    '2': 'Zero Hunger',
    '3': 'Good Health and Well-being',
    '4': 'Quality Education',
    '5': 'Gender Equality',
    '6': 'Clean Water and Sanitation',
    '7': 'Affordable and Clean Energy',
    '8': 'Decent Work and Economic Growth',
    '9': 'Industry, Innovation and Infrastructure',
    '10': 'Reduced Inequality',
    '11': 'Sustainable Cities and Communities',
    '12': 'Responsible Consumption and Production',
    '13': 'Climate Action',
    '14': 'Life Below Water',
    '15': 'Life on Land',
    '16': 'Peace, Justice and Strong Institutions',
    '17': 'Partnerships for the Goals'
}

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
    </style>
""", unsafe_allow_html=True)

# ===== Header =====
st.markdown("<div class='main-title'>KMITL SDG Matching for All</div>", unsafe_allow_html=True)
st.markdown("""
    <div class='subtitle'>
        🔍 เช็กข้อความของคุณว่าสอดคล้องกับเป้าหมายการพัฒนาที่ยั่งยืน (SDGs) ข้อใดบ้าง<br>
        รองรับทั้ง <strong>ภาษาไทย</strong> และ <strong>ภาษาอังกฤษ</strong>
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
                        st.markdown(f"<div style='display:flex; align-items:center; height:50px;'><span style='font-size:22px; color:#444; font-weight:600; line-height:1;'>SDG {sdg}: {name}</span></div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<span style='font-size:22px; color:#444; font-weight:600;'>SDG {sdg}: {name}</span>", unsafe_allow_html=True)

            # ===== Show Hashtag Box (With Copy Button) =====
            base_hashtags = "#KMITL #สจล #พระจอมเกล้าลาดกระบัง"
            sdg_hashtags = ' '.join([f"#SDG{sdg}" for sdg in matched_sdgs])
            full_hashtags = base_hashtags + "\n" + sdg_hashtags

            st.markdown("### ✨ สรุปการวิเคราะห์ (Hashtag)")
            st.code(full_hashtags, language=None)
        else:
            st.info("ไม่พบคำที่ตรงกับ SDGs ในข้อความนี้")

# ===== Footer =====
st.markdown("""
    <div style='text-align:center; margin-top: 80px; font-size: 14px; color: #666;'>
        © 2025 Office of Strategy Management KMITL
    </div>
""", unsafe_allow_html=True)
