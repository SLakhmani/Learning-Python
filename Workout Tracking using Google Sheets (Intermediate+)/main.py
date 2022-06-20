import requests
import os
from datetime import datetime

# Sensitive information varies with user and is stored in environment variables
APP_ID = os.environ.get("APP_ID")
APP_API_KEY = os.environ.get("APP_API_KEY")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

# Header for Authentication with Nutritionix
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_API_KEY,
    "x-remote-user-id": "0",
}
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

query_params = {
    "query": input("What exercises did you do?: "),
}

nutritionix_response = requests.post(url=nutritionix_endpoint, json=query_params, headers=headers).json()
exercise_data = nutritionix_response["exercises"]

today = datetime.now()
date_formatted = today.strftime("%d/%m/%Y")
time_formatted = today.strftime("%H:%M:%S")

# Header for Authentication with Sheety
sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
}

for exercise in exercise_data:
    sheety_data = {
        "workout": {
            "date": date_formatted,
            "time": time_formatted,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_data, headers=sheety_headers)

print("Google sheets updated with exercise information!")
