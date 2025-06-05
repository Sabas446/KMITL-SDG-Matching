import gspread
import pandas as pd
import datetime
import streamlit as st
import json
from oauth2client.service_account import ServiceAccountCredentials

SHEET_NAME = "sdg_counter"

def log_action_to_sheet(action):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds_dict = json.loads(st.secrets["GSP_CREDENTIALS"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    sheet = client.open(SHEET_NAME).worksheet("logs")

    now = datetime.datetime.now().isoformat()
    user_agent = st.request.headers.get("user-agent", "unknown")
    query = st.query_params

    sheet.append_row([now, action, user_agent, str(query)])

def get_stats_from_logs():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds_dict = json.loads(st.secrets["GSP_CREDENTIALS"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
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
