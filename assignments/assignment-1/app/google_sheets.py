from google.oauth2 import service_account
from googleapiclient.discovery import build

def authenticate_google_sheets():
    try:
        credentials = service_account.Credentials.from_service_account_file(
            'C:\Users\Checkout\mini_reverse_etl\reverseetl-401022-c2b0bcbcfd58.json',
            scopes=['https://www.googleapis.com/auth/spreadsheets']
        )
        sheets_service = build('sheets', 'v4', credentials=credentials)
        return sheets_service
    except Exception as e:
        print("Error authenticating with Google Sheets:", str(e))
        return None

def push_data_to_sheets(data):
    try:
        sheets_service = authenticate_google_sheets()
        if sheets_service:
            spreadsheet_id = 'your_spreadsheet_id'
            range_name = 'customer'  # Name of the sheet
            values = [
                [row["customer_id"], row["first_name"], row["last_name"], row["email"]]
                for row in data
            ]
            
            body = {
                'values': values
            }
            
            # Write data to the sheet
            result = sheets_service.spreadsheets().values().update(
                spreadsheetId=spreadsheet_id, range=range_name,
                valueInputOption='RAW', body=body).execute()
            
            return True
            
    except Exception as e:
        print("Error pushing data to Google Sheets:", str(e))
        return False
