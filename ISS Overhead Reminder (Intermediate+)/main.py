import requests
import datetime as dt
import smtplib
import time

MESSAGE_BODY = "Subject:Look Up!\n\nTHE ISS IS OVERHEAD!"
PASSWORD = "yourpassword"
EMAIL = "sender_email@example.com"
RECEIVER_EMAIL = "receiver_email@example.com"

MY_LAT = 52.205338
MY_LONG = 0.121817


def is_iss_close():  # Check if the ISS is within +5 or -5 degrees from current location
    response_iss = requests.get("http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()

    iss_data = response_iss.json()

    iss_lng = float(iss_data["iss_position"]["longitude"])
    iss_lat = float(iss_data["iss_position"]["latitude"])

    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_lng <= MY_LONG + 5:
        return True


def is_it_night():  # Check if it is night time in current location
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response_sun = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response_sun.raise_for_status()
    sun_data = response_sun.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True


while True:
    time.sleep(60)  # Check every 60 seconds
    if is_iss_close() and is_it_night():  # Send email reminder if ISS is close and it is night time
        try:
            with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
                connection.starttls()
                connection.login(EMAIL, PASSWORD)
                connection.sendmail(EMAIL, RECEIVER_EMAIL, MESSAGE_BODY)
        except:
            print("Unable to send email...")
        else:
            print("Email sent!")
