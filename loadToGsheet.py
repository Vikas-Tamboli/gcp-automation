import gspread
import pandas as pd
from google.auth import default
from gspread_dataframe import set_with_dataframe
import datetime

scopes = [
    "https://www.googleapis.com/auth/cloud-platform",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/drive.file",
]
# credentials = Credentials.from_authorized_user_file('/google/secrets/google_default_credentials.json', scopes=SCOPES)
credentials, project = default(quota_project_id="searce-msp-gcp", scopes=scopes)
gspread_client = gspread.authorize(credentials)
gsheet = gspread_client.open_by_url("https://docs.google.com/spreadsheets/d/1qBXcYOWeNxXPKhdSh9MFeziN67eIHoEMN6EUB2ujhnU")

#ws = gsheet.worksheet("Sheet2")
today = datetime.date.today()
sheet_name = today.strftime("%Y-%m-%d")
print (sheet_name)

gsheet.add_worksheet(title=sheet_name, rows=100, cols=20)

df = pd.read_csv('file.csv')

ws = gsheet.worksheet(sheet_name)
set_with_dataframe(ws, df)
