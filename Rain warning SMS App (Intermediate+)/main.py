import requests
from twilio.rest import Client

twilio_sid = "examplesidfortwilio"
twilio_auth_token = "exampleauthtokenfortwilio"

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "owm_api_key_example"
NUM_HOURS = 12  # How many hours to check for, from running the script 
MY_LAT = 52.202541  # Your geo location
MY_LON = 0.131240


parameters = {
    "lat": 26.144518,
    "lon": 91.736237,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
}

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

hourly_data = weather_data["hourly"][:NUM_HOURS]
hourly_weather_ids = []

will_rain = False
for hour in hourly_data:
    condition_id = hour["weather"][0]["id"]
    if int(condition_id) < 700:
        will_rain = True

if will_rain:
    # send reminder via sms
    client = Client(twilio_sid, twilio_auth_token)
    message = client.messages.create(body="It's going to rain.", from_="example_twilio_phone_num", to="example_verified_ph_no")
    print(message.status)
