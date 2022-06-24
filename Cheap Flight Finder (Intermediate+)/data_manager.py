import requests
import os


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.API_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
        self.EMAILS_ENDPOINT = os.environ.get("EMAILS_ENDPOINT")

    def get_sheet_data(self):
        response = requests.get(self.API_ENDPOINT)
        sheet_data = response.json()["prices"]
        return sheet_data

    def update_sheet_data(self, row_id, row):
        row_endpoint = self.API_ENDPOINT + f"/{row_id}"
        row_data = {
            "price": row
        }

        response = requests.put(row_endpoint, json=row_data)
        response.raise_for_status()

    def get_emails(self):
        response = requests.get(self.EMAILS_ENDPOINT)
        user_data = response.json()["users"]
        email_list = []
        for users in user_data:
            email_list.append((users["email"], users["firstName"]))
        return email_list
