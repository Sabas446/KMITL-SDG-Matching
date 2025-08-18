import streamlit as st
import time
from matcher import match_with_explanations
import os
import re, html

# ===== Page Configuration =====

st.set_page_config(page_title="KMITL SDG Matching for All", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
/* ========== Base & Card ========== */
:root{
  --brand:#f26f21;
  --bg:#fff;
  /* type scale with minimums */
  --fz-base:  clamp(13px, 1.6vw, 16px);
  --fz-h1:    clamp(26px, 5.2vw, 40px);
  --fz-h2:    clamp(18px, 3.6vw, 28px);
  --fz-h3:    clamp(16px, 3.0vw, 22px);
  --fz-sdg:   clamp(14px, 2.4vw, 18px);
  --fz-small: clamp(11px, 2.0vw, 14px);
}

.stApp{ background: var(--bg); }

.block-container{
  max-width: min(1080px,94vw);
  margin: 72px auto 36px !important;
  padding: 12px 24px 24px !important;
  background: #fff;
  border-radius: 18px;
  border: 1px solid rgba(0,0,0,.06);
  box-shadow: 0 12px 30px rgba(0,0,0,.08);
  position: relative;
  overflow: visible;
  isolation: isolate;
}


/* ========== Typography ========== */
.stApp, .stApp p, .stApp li{ font-size: var(--fz-base); line-height:1.55; }
.block-container h1{ font-size: var(--fz-h1) !important; line-height:1.15; margin: 2px 0 6px !important; }
.block-container h2{ font-size: var(--fz-h2) !important; }
.block-container h3{ font-size: var(--fz-h3) !important; }
.block-container > :first-child{ margin-top: 0 !important; }
.block-container hr{ margin: .4rem 0 !important; }

/* Header area (ของคุณมี .flex-header / .responsive-title / .subtitle) */
.flex-header{ display:flex; align-items:center; justify-content:center; gap:12px; margin:6px 0 10px; flex-wrap:wrap; font-size: var(--fz-h1)}
.flex-header img{ width: clamp(28px,5vw,48px); height:auto; }
.responsive-title{ color: var(--brand); text-align:center; font-weight:800; }
.subtitle{ text-align:center; font-size: var(--fz-sdg) !important; }

/* Inputs/Buttons */
.stTextArea label{ font-size: var(--fz-sdg) !important; font-weight:700; }
.stTextArea textarea{ font-size: var(--fz-base) !important; padding:1em; }
.stButton > button{
  background: var(--brand); color:#fff; font-weight:700;
  font-size: clamp(16px,4vw,22px); padding:.5em 1.2em; border-radius:12px; border:none;
}
.stButton > button:hover{ background:#d95400; }

/* Alerts & code blocks */
div[data-testid="stAlert"] p{ font-size: var(--fz-base) !important; }
div[data-testid="stCode"] pre{
  font-size: var(--fz-base) !important; padding:8px 10px !important;
  white-space: pre-wrap !important; word-break: break-word !important; overflow-wrap:anywhere !important;
}

/* ======= SDG row (icon + title) ======= */
/* จับเฉพาะแถวคอลัมน์ที่มีรูป SDG และข้อความ .sdg-result แล้วทำเป็น 'grid' 2 คอลัมน์: 50px + 1fr */
.block-container [data-testid="stHorizontalBlock"]:has(img):has(.sdg-result){
  display: grid !important;
  grid-template-columns: 50px 1fr !important;
  column-gap: 10px !important;
  align-items: start !important;
  flex-wrap: nowrap !important;  /* เผื่อธีมตั้งค่าเป็น flex */
  margin: 6px 0 !important;
}

/* คอลัมน์รูป = กว้างคงที่ 50px; รูป = 50px คงที่เสมอ */
.block-container [data-testid="stHorizontalBlock"]:has(img):has(.sdg-result) > div:has(img){
  max-width: 50px !important; width: 50px !important; flex: 0 0 50px !important;
}
.block-container [data-testid="stHorizontalBlock"]:has(img):has(.sdg-result) > div:has(img) img{
  width: 50px !important; height:auto !important; max-width:none !important;
}

/* คอลัมน์ข้อความ = กินพื้นที่ที่เหลือ และห่อบรรทัดในคอลัมน์เอง */
.block-container [data-testid="stHorizontalBlock"]:has(img):has(.sdg-result) > div:not(:has(img)){
  min-width: 0 !important;    /* ป้องกันข้อความดันกริดล้น */
}

/* บางธีมแอบตั้ง div สูง 50px ทำให้ชื่อลอย—รีเซ็ต */
.block-container [data-testid="stHorizontalBlock"]:has(img):has(.sdg-result)
  > div:not(:has(img)) div[style*="height:50px"]{
  height:auto !important; display:block !important;
}

/* สไตล์ชื่อ SDG */
.sdg-result{
  font-size: var(--fz-sdg) !important;
  line-height:1.35; padding:4px 8px;
}

/* Highlight */
mark.hl{ padding:0 .25em; border-radius:.25rem; background:#fff2e9; box-shadow: inset 0 0 0 1px rgba(242,111,33,.25); }

/* Footer */
.footer{ max-width: 90ch; margin: 18px auto 0; text-align:center; }
.footer, .footer em, .footer small{
  font-size: var(--fz-small) !important; line-height:1.6;
  overflow-wrap:anywhere; word-break:normal; hyphens:auto; text-wrap:pretty;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* ---------- 1) ชื่อ SDG เป็นตัวเข้ม ---------- */
.sdg-result, .sdg-title{
  font-weight: 800 !important;      /* เข้มกว่าเดิม */
  font-size: clamp(13px, 2.4vw, 18px);
  line-height: 1.33 !important;     /* ชิดขึ้นเล็กน้อย */
}

/* ---------- 2) บีบระยะบรรทัด/มาร์จินตอนจอแคบ ---------- */
@media (max-width: 540px){
  .stApp, .stApp p, .stApp li{ line-height: 1.45 !important; }   /* เนื้อความ */
  .block-container li{ margin: .08rem 0 !important; }            /* bullet */
  .sdg-result, .sdg-title{ line-height: 1.28 !important; }       /* แถวชื่อ SDG */
  .block-container h1{ margin: .15rem 0 .3rem !important; }
  .block-container h2, .block-container h3{ margin: .3rem 0 !important; }
  .block-container hr{ margin: .2rem 0 !important; }
  div[data-testid="stAlert"] p{ margin: .3rem 0 !important; }
}

/* ---------- 3) ธีมสี สจล. (หัวข้อใหญ่ + ปุ่ม) ---------- */
:root{
  --brand:#f26f21;          /* KMITL Orange */
  --brand-2:#ff9d3d;        /* Orange Light */
  --brand-dark:#d95400;     /* Hover */
}

/* หัวข้อใหญ่ให้เป็นตัวอักษรไล่สี (อ่านชัด มืออาชีพ) */
.responsive-title{
  background: linear-gradient(100deg, var(--brand), var(--brand-2));
  -webkit-background-clip: text; background-clip: text;
  color: transparent !important;
  text-shadow: 0 1px 0 rgba(0,0,0,.04);
}

/* ปุ่มหลักให้เข้าธีม สจล. */
.stButton > button{
  background: linear-gradient(100deg, var(--brand), var(--brand-2)) !important;
  color:#fff !important; border:none !important;
  font-weight:700; border-radius:12px;
  box-shadow: 0 6px 16px rgba(242,111,33,.25);
  transition: transform .06s ease, filter .2s ease;
}
.stButton > button:hover{
  filter: brightness(.97);
  background: linear-gradient(100deg, var(--brand-dark), var(--brand-2)) !important;
  transform: translateY(-1px);
}
.stButton > button:active{ transform: translateY(0); }

/* (ไม่จำเป็น) เส้นสีบนกล่องให้เข้าธีม */
.block-container::before{
  background: linear-gradient(90deg, var(--brand), var(--brand-2));
}

/* หัวข้อ/หัวข้อย่อยให้เด่นแบบ brand */
.responsive-title{
  background: linear-gradient(100deg,#f26f21,#ff9d3d);
  -webkit-background-clip:text; background-clip:text; color:transparent !important;
}
.block-container h2, .block-container h3{
  font-weight:800 !important;
  position: relative;
  padding-left:.65rem;
}
.block-container h2::before, .block-container h3::before{
  content:""; position:absolute; left:0; top:.2em; bottom:.2em; width:4px;
  border-radius:3px; background:linear-gradient(180deg,#f26f21,#ffb14a);
}

/* กล่องแฮชแท็กให้ดูคล้าย ‘pill container’ */
div[data-testid="stCode"] pre{
  background:#0b0f140a !important;   /* light: จางๆ */
  border:1px solid rgba(0,0,0,.08) !important;
  border-radius:12px !important; padding:8px 10px !important;
  white-space:pre-wrap !important; word-break:break-word !important;
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



# ===== Header =====

st.markdown("""
<div class="flex-header">
    <div class="responsive-title">KMITL SDG Matching for All</div>
    <img src="https://raw.githubusercontent.com/Sabas446/KMITL-SDG-Matching/main/osm_logo.png">
</div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class='subtitle'>
        🔍 เช็กข้อความว่าสอดคล้องกับเป้าหมายการพัฒนาที่ยั่งยืน (SDGs) ใดบ้าง<br>
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
            st.markdown("### 📝 คำที่เชื่อมโยงกับ SDG (Highlight) จากข้อความที่กรอก ")

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
                    cols = st.columns([0.05, 0.95])
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
