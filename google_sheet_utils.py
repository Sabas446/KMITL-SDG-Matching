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

def log_action_to_sheet(action):
    creds = get_credentials()
    client = gspread.authorize(creds)
    sheet = client.open(SHEET_NAME).worksheet("logs")
    now = datetime.datetime.now(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([now, action])

def get_stats_from_logs():
    creds = get_credentials()
    client = gspread.authorize(creds)
    sheet = client.open(SHEET_NAME).worksheet("logs")
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce", utc=True)
    df["timestamp"] = df["timestamp"].dt.tz_convert("Asia/Bangkok")

    now = datetime.datetime.now()
    df_month = df[(df["timestamp"].dt.month == now.month) & (df["timestamp"].dt.year == now.year)]

    total_visits = df[df["action"] == "visit"].shape[0]
    total_checks = df[df["action"] == "check"].shape[0]
    month_visits = df_month[df_month["action"] == "visit"].shape[0]
    month_checks = df_month[df_month["action"] == "check"].shape[0]

    return total_visits, total_checks, month_visits, month_checks
