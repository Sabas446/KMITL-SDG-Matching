import streamlit as st
import time
from matcher import match_with_explanations
import os
import re, html

# ===== Page Configuration =====

st.set_page_config(page_title="KMITL SDG Matching for All", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
.block-container{ padding-top: 1rem; }      /* ลดบนทั้งหน้า */
hr{ margin: .5rem 0 !important; }           /* ถ้ามีเส้นคั่นจะไม่กินพื้นที่ */
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* จอที่กว้างมากค่อยบีบหน้าให้แคบลง = 4/6 ของจอ แล้วจัดกลาง */
@media (min-width: 1280px){
  .block-container{
    max-width: 66.666vw;   /* 4 ส่วนจาก 6 */
    margin-left: auto;
    margin-right: auto;
  }
}
</style>
""", unsafe_allow_html=True)

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
        🔍 เช็กข้อความของคุณว่าสอดคล้องกับเป้าหมายการพัฒนาที่ยั่งยืน (SDGs) ใดบ้าง<br>
        รองรับทั้ง <strong>ภาษาไทย</strong> และ <strong>ภาษาอังกฤษ</strong><br>
    </div>
""", unsafe_allow_html=True)
st.markdown("---")

# ===== Input and Submit =====

text_input = st.text_area("📥 กรุณาใส่ข้อความที่ต้องการตรวจสอบ:", height=300)
if st.button("🔍 วิเคราะห์"):
    if text_input.strip() == "":
        st.warning("⚠️ กรุณาใส่ข้อความก่อนกด วิเคราะห์")
    else:
        matched_sdgs, explanations = match_with_explanations(text_input)
        # normalize types so UI and matcher agree
        matched_sdgs = [int(s) for s in matched_sdgs]
        explanations = {int(k): v for k, v in explanations.items()}
        if matched_sdgs:
            matched_sdgs = sorted(matched_sdgs, key=lambda x: int(x))
            st.success(f"✅ พบ {len(matched_sdgs)} เป้าหมายที่เกี่ยวข้อง")

            # ===== Toggle ไฮไลต์ข้อความ =====
            st.markdown("##### 📝 คำที่เชื่อมโยงกับ SDG (Highlight) จากข้อความที่กรอก ")

            raw_text = text_input  # เก็บต้นฉบับ
            # ดึง terms จาก explanations
            terms = []
            for msgs in (explanations or {}).values():
                for m in msgs or []:
                    s = str(m).strip().replace("\u200b", "")
                    m1 = re.search(r"ค้นพบคำว่า (.+?) ซึ่งอยู่ใน Layer", s)
                    if not m1:
                        m1 = re.search(r"ค้นพบว่า (.+?) ซึ่งเป็น Keyword ของ SDG", s)  # เผื่ออนาคต fallback/post
                    if m1:
                        terms.append(m1.group(1))

            # กันซ้ำ + เรียงคำยาวก่อน (กันซ้อนทับ)
            terms = sorted(set(terms), key=lambda x: -len(x))

            def build_spans(text: str, terms: list[str]):
                spans = []
                lower = text.lower()
                occupied = [False] * len(text)

                for term in terms:
                    if not term: 
                        continue
                    pattern = re.escape(term)
                    for m in re.finditer(pattern, lower, flags=re.IGNORECASE):
                        s, e = m.start(), m.end()
                        if any(occupied[s:e]):  # ถ้าทับกับช่วงที่ทำเครื่องหมายไว้แล้ว ให้ข้าม
                            continue
                        for i in range(s, e):
                            occupied[i] = True
                        spans.append((s, e))
                spans.sort()
                return spans

            def render_highlight(text: str, spans: list[tuple[int,int]]):
                out, last = [], 0
                for s, e in spans:
                    out.append(html.escape(text[last:s]))
                    out.append(f"<mark class='hl'>{html.escape(text[s:e])}</mark>")
                    last = e
                out.append(html.escape(text[last:]))
                return "".join(out)

            spans = build_spans(raw_text, terms)

            # แสดงผลตามสถานะ toggle
            if spans:
                st.markdown(
                    """
                    <style>
                    mark.hl { padding: 0 .2em; border-radius: .25rem; }
                    </style>
                    """,
                    unsafe_allow_html=True
                )
                st.markdown(render_highlight(raw_text, spans), unsafe_allow_html=True)
            else:
                # แสดงต้นฉบับ (ล็อกแก้ไข เพื่อไม่งงว่ากล่องนี้คือผลลัพธ์)
                st.text_area("ข้อความต้นฉบับ", value=raw_text, height=220, disabled=True)


            for sdg in matched_sdgs:
                name = sdg_names.get(str(sdg), f'SDG {sdg}')
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

                # ===== อธิบายเชิงมืออาชีพ ตามรูปประโยคที่คุณต้องการ =====
                msgs = explanations.get(sdg) or explanations.get(str(sdg), [])
                if msgs:
                    for m in sorted(set(msgs)):  # กันซ้ำเล็กน้อย
                        st.markdown(f"- {m}")
                        
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
