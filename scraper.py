# scraper.py
# Created by Anubhav Nigam on 1/20/21
# Copyright © Anubhav Nigam. All rights reserved

from __future__ import print_function
from googlesearch import search
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from oauth2client.service_account import ServiceAccountCredentials
import gspread
gc = gspread.oauth()


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# ID and range of spreadsheet
sheet_id = '1vVwnG6BgqjBM9pYOV5jXfOD8SexR-D64gg8ck8KTIhE'
read_range = 'A2:E1931'

def main():
    # reads/writes values from/to spreadsheet https://docs.google.com/spreadsheets/d/1vVwnG6BgqjBM9pYOV5jXfOD8SexR-D64gg8ck8KTIhE/edit#gid=0
    creds = None
    # token.pickle stores access and refresh tokens and is created automatically when the auth flow is completed the first time
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available the user must login.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials = creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId = sheet_id,
                                range = read_range).execute()
    values = result.get('values', [])

    sh = gc.open("College thing")
    ws = sh.get_worksheet(0)
    current_row = 1

    if not values:
        print('No data found.')
    else:
        print('Query: ')
        for row in values:
            current_row += 1
            query = row[0] + " common data set 2018 filetype:pdf"
            print(row[0])

            for j in search(query, tld = "co.in", num = 1, stop = 1, pause = 3):
                temp = '%s' % j
                if temp.find("Common") != -1 or temp.find("Data") != -1 or temp.find("common") != -1 or temp.find("data") != -1:
                    cds_link = temp
                else:
                    cds_link = 'no public CDS'
                print(cds_link)
                ws.update_cell(current_row, 5, cds_link)

if __name__ == '__main__':
    main()