from flask import Flask, render_template, request, redirect, url_for, session
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import os

app = Flask(__name__)
app.secret_key = '' 

# Path to the service account credentials file
# CREDENTIALS_FILE = 'gs_credentials.json'
credentials_info = json.loads(os.environ.get('GOOGLE_CREDENTIALS'))
CREDENTIALS_FILE = 'your_credentials.json'

# # Define the scope for the API
SCOPES = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# # SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

# Load the credentials and create a client to interact with the Google Sheets API
creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_info, SCOPES)
client = gspread.authorize(creds)

# The name of your Google Sheet
SHEET_NAME = 'Add_your_spreadsheet'
SHEET = client.open(SHEET_NAME)
worksheet = SHEET.sheet


def save_to_google_sheets(name, email, role, recommend, languages, comment):
    worksheet.append_row([name, email, role, recommend, ','.join(languages), comment])
 
        

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']
        recommend = request.form['recommend']
        languages = request.form.getlist('languages[]')
        comment = request.form['comment']

        save_to_google_sheets(name, email, role, recommend, languages, comment)
        # worksheet.append_row([name, email, role, recommend, ','.join(languages), comment])

        session['welcome_message'] = {
            'Name': name,
            'Email': email,
            'Role': role,
            'Recommend': recommend,
            'Languages': ', '.join(languages),
            'Comment': comment
        }

        return redirect(url_for('display_info'))

    return render_template('first.html')

@app.route('/display_info')
def display_info():
    welcome_message = session.get('welcome_message', {})
    return render_template('display_info.html', welcome_message=welcome_message)

if __name__ == '__main__':
    app.run(debug=True)

# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# from pprint import pprint



# # Path to the service account credentials file
# CREDENTIALS_FILE = 'gs_credentials.json'

# # Define the scope for the API
# SCOPES = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# # SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

# # Load the credentials and create a client to interact with the Google Sheets API
# creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, SCOPES)
# client = gspread.authorize(creds)
# sheet = client.open('Information').sheet1
# data = sheet.get_all_records()
# pprint(data)
# sheet.delete_(6,1,"Aamir")