import requests
import os


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.API_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

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
