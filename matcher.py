from full_context_reasoning import full_context_reasoning, reason_tracer

def match_with_explanations(text: str, top_k_per_sdg: int = 2):
    tx = (text or "").lower()
    matched = set(full_context_reasoning(tx))

    # รวบรวม hits ทั้งหมดที่ใช้ได้
    hits = [h for h in reason_tracer(tx) if h["sdg"] in matched]

    # จัดกลุ่มตาม SDG
    by_sdg = {}
    for h in hits:
        by_sdg.setdefault(h["sdg"], []).append(h)

    explanations = {}
    for sdg, hs in by_sdg.items():
        # เรียง: คำยาว/เฉพาะก่อน แล้วค่อยชั้นเลเยอร์ต่ำกว่า
        hs = sorted(hs, key=lambda h: (-len(h["term"]), h["layer"], h["term"]))

        keep, seen = [], []
        for h in hs:
            t = h["term"]
            # ตัดคำที่เป็นซับสตริงกันเอง เช่น มี "reduce inequality" แล้วตัด "inequality"
            if any(t in s or s in t for s in seen):
                continue
            seen.append(t)
            keep.append(h)
            if len(keep) == top_k_per_sdg:
                break

        explanations[sdg] = [
            f'ค้นพบคำว่า {h["term"]} ซึ่งอยู่ใน Layer {h["layer"]}: {h["layer_name"]}'
            for h in keep
        ]

    return sorted(matched), explanations
