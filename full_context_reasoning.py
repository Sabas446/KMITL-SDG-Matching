# ======= Single-source matching: LAYER_NAMES + TERMS =======
from typing import Dict, List

# ถ้ามี LAYER_NAMES อยู่แล้วจะใช้ของเดิม, ถ้าไม่มีก็สร้างเปล่าไว้ก่อน
try:
    LAYER_NAMES  # already defined above
except NameError:
    LAYER_NAMES: Dict[str, Dict[int, str]] = {str(i): {} for i in range(1, 18)}
    
from sdg_layer_names_full import apply_full_layer_names
apply_full_layer_names(LAYER_NAMES)


# ฐานคำแบบชั้น (1..9) ต่อ SDG (1..17)
TERMS: Dict[str, Dict[int, tuple]] = {}

# ----- ฟังก์ชันเดียวสำหรับเพิ่มคำ (แกนของระบบ) -----
def add_terms(sdg: int | str, layer: int, words: List[str], layer_name: str = None):
    """
    เพิ่มคำเข้า TERMS แบบกันซ้ำ + ตั้งชื่อเลเยอร์ได้ในที่เดียว
    ใช้ซ้ำได้เรื่อย ๆ เช่น add_terms(12, 3, ["recycling"], "Waste reduction/recycling")
    """
    s = str(sdg)
    LAYER_NAMES.setdefault(s, {})
    if layer_name:
        LAYER_NAMES[s][layer] = layer_name
    TERMS.setdefault(s, {}).setdefault(layer, tuple())

    base = set(map(str.lower, TERMS[s][layer]))
    base |= {w.lower() for w in words if isinstance(w, str) and w.strip()}
    TERMS[s][layer] = tuple(sorted(base))

import importlib.util, pathlib, sys

def _load_terms_from_auto():
    # เรียกใช้หลังจากนิยาม add_terms() แล้วเท่านั้น
    path = pathlib.Path(__file__).with_name('add_terms_auto.py')
    spec = importlib.util.spec_from_file_location("add_terms_auto_runtime", str(path))
    mod = importlib.util.module_from_spec(spec)
    # inject ให้ไฟล์ add_terms_auto.py ใช้ add_terms ของไฟล์นี้
    mod.add_terms = add_terms
    sys.modules["add_terms_auto_runtime"] = mod
    spec.loader.exec_module(mod)
    
    if hasattr(mod, "register_all_terms"):
        mod.register_all_terms(add_terms)
    
# โหลด keyword ทั้งหมดจาก add_terms_auto.py
_load_terms_from_auto()

# ====== สแกนเนอร์กลาง + อธิบายเหตุผล + กฎกันโอเวอร์เคลม ======
def _scan_terms(text: str):
    t = _normalize(text)
    hits = []
    for sdg in map(str, range(1, 18)):  # เรียง SDG 1..17 เสมอ
        layers = TERMS.get(sdg, {})
        for layer in range(1, 10):      # เรียง Layer 1..9 เสมอ
            for kw in layers.get(layer, ()):
                if kw and kw in t:
                    hits.append({
                        "sdg": sdg,
                        "layer": layer,
                        "term": kw,
                        "layer_name": LAYER_NAMES.get(sdg, {}).get(layer, f"Layer {layer}")
                    })
    return hits

import re, unicodedata

def _normalize(t: str) -> str:
    t = unicodedata.normalize("NFC", t or "")
    # ตัด zero-width + # แฮชแท็ก (กันเคส #คำ)
    t = re.sub(r"[\u200b\ufeff#]", "", t)
    return t.lower()

def reason_tracer(text: str):
    # เรียงผลลัพธ์: SDG (1..17) แล้วค่อย Layer (1..9) แล้วค่อย term
    hits = _scan_terms(_normalize(text))
    return sorted(hits, key=lambda h: (int(h["sdg"]), h["layer"], h["term"]))

def full_context_reasoning(text: str):
    tx = _normalize(text)
    hits = _scan_terms(tx)
    matched = {h["sdg"] for h in hits}

    # กันโอเวอร์เคลม SDG 4 ถ้าไม่มีสัญญาณชัดจาก L1 และไม่มีคำหลักสำคัญ
    has_core4 = any(h["sdg"] == "4" and h["layer"] == 1 for h in hits)
    if '4' in matched and not has_core4 and not any(w in tx for w in
        ["education","training","school","learning","literacy","การศึกษา","การฝึกอบรม","การเรียนรู้","การรู้หนังสือ"]):
        matched.discard('4')

    return sorted(matched, key=lambda s: int(s))
