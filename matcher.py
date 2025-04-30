
# matcher.py (reasoning-driven version)

import pandas as pd
import re
from full_context_reasoning import full_context_reasoning

# Load keywords from Excel
keyword_file = "sdg_keywords.xlsx"
keywords_df = pd.read_excel(keyword_file)

# Prepare keyword list
keywords = {}
for index, row in keywords_df.iterrows():
    sdg_number = str(row['SDG'])
    keyword_text = str(row['Keyword']).strip().lower()

    if sdg_number not in keywords:
        keywords[sdg_number] = set()

    if keyword_text:
        keywords[sdg_number].add(keyword_text)

# Match text to SDGs
def match_text(text):
    text = str(text).lower()
    matched_sdgs = set()

    # (1) ใช้ Full Context Reasoning วิเคราะห์ก่อน
    context_sdgs = full_context_reasoning(text)
    matched_sdgs.update(context_sdgs)

    # (2) ถ้ายังไม่เจอ SDG ใดเลย ➔ fallback มาหา keyword matching
    if not matched_sdgs:
        for sdg, kw_set in keywords.items():
            for kw in kw_set:
                if kw in text:
                    matched_sdgs.add(sdg)
                    break

    return sorted(list(matched_sdgs))
