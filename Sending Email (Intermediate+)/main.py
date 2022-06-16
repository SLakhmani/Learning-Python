import smtplib
import datetime as dt
import random

day_of_the_week = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

# Get current date and time
now = dt.datetime.now()
current_day = now.weekday()

# If today is thursday, send Email
if day_of_the_week[current_day] == "Thursday":
    try:
        with open("quotes.txt") as quotes_file:
            contents = quotes_file.readlines()
            quote_to_send = random.choice(contents)
    except FileNotFoundError:
        print("Could not locate file...")
    else:
        # Send Email
        my_email = "sender_email@yahoo.com"  # Email you are sending from
        to = "receiver_email@gmail.com"  # Email you are sending to
        password = "P@$$w0rD"  # Password usd to log in to your email
        msg_txt = f"Subject:Have A Nice Day!\n\n{quote_to_send}"  # Message body
        try:
            with smtplib.SMTP("smtp.mail.yahoo.com") as server:  # Establishing connection with mail client
                server.starttls()  # TLS for security
                server.login(user=my_email, password=password)
                server.sendmail(from_addr=my_email, to_addrs=to, msg=msg_txt)
        except:
            print("There was a problem sending the Email...")
        else:
            print("Email sent!")
