import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import datetime
from datetime import timezone, timedelta
import streamlit as st

SHEET_NAME = "sdg_counter"

def get_credentials():
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
    return creds

def log_action_to_sheet(action, timestamp=None):
    creds = get_credentials()
    client = gspread.authorize(creds)
    sheet = client.open(SHEET_NAME).worksheet("logs")

    # 🧹 ลบแถวสุดท้ายถ้าเป็น "bot"
    values = sheet.get_all_values()
    last_row_index = len(values)
    if values and len(values[-1]) >= 2:
        last_action = values[-1][1]
        if last_action == "bot":
            sheet.delete_rows(last_row_index)

    # 🕒 สร้าง timestamp ถ้ายังไม่ได้ส่งมา
    if timestamp is None:
        timestamp = datetime.datetime.now(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S")

    sheet.append_row([timestamp, action])

def get_stats_from_logs():
    creds = get_credentials()
    client = gspread.authorize(creds)
    sheet = client.open(SHEET_NAME).worksheet("logs")
    
    values = sheet.get_all_values()
    # ✅ ตัด header
    df = pd.DataFrame(values[1:], columns=["timestamp", "action"])

    # ✅ กรอง bot ออก
    df = df[df["action"] != "bot"]
    
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce", utc=True)
    df["timestamp"] = df["timestamp"].dt.tz_convert("Asia/Bangkok")

    now = datetime.datetime.now(timezone(timedelta(hours=7)))
    df_month = df[(df["timestamp"].dt.month == now.month) & (df["timestamp"].dt.year == now.year)]

    total_visits = df[df["action"].str.startswith("visit")].shape[0]
    total_checks = df[df["action"] == "check"].shape[0]
    month_visits = df_month[df_month["action"].str.startswith("visit")].shape[0]
    month_checks = df_month[df_month["action"] == "check"].shape[0]

    return total_visits, total_checks, month_visits, month_checks
    
def get_last_logged_timestamp():
    creds = get_credentials()
    client = gspread.authorize(creds)
    sheet = client.open(SHEET_NAME).worksheet("logs")
    values = sheet.get_all_values()
    for row in reversed(values):
        if len(row) >= 2 and row[1] in ["visit", "bot"]:
            try:
                return datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S").replace(
    tzinfo=timezone(timedelta(hours=7))
).timestamp()

            except:
                continue
    return None
