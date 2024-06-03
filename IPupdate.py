import threading
from requests import get
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

#IPaddress.json should be the name of the file with your private API key details you can change the name of the file or replace this
#with the json key you have created for Google Sheets
creds = ServiceAccountCredentials.from_json_keyfile_name('IPaddress.json',scope)
client = gspread.authorize(creds)

#replace the name of your sheet name here mine was "minecraft IP"
sheet = client.open('minecraft IP').sheet1
upd = sheet.get_all_records()
def printit():
  try:
    threading.Timer(60.0, printit).start()
    ip = get('https://api.ipify.org').text
    sheet.update_cell(1,1, ip)
    print(sheet.cell(1,1))
  except:
    print("Internet is down currently.")
printit()