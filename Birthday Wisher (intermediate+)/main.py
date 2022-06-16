import smtplib
import random
import pandas
import datetime as dt

SUBJECT = "Happy Birthday You!\n\n"
SENDER_NAME = "Your Name"
SENDER_EMAIL = "youremail@yahoo.com"
SENDER_PASSWORD = "yourpassword"


def construct_email(letter_body):
    return f"Subject:{SUBJECT}{letter_body}"


def send_emails(mailing_list):
    sent_emails = []
    for (receiver_email, message) in mailing_list.items():
        message_body = construct_email(message)
        try:
            with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
                connection.starttls()
                connection.login(SENDER_EMAIL, SENDER_PASSWORD)
                connection.sendmail(SENDER_EMAIL, receiver_email, message_body)
        except:
            print(f"Unable to end email to: {receiver_email}")
        else:
            sent_emails.append(receiver_email)
    return sent_emails


date_today = dt.datetime.now()
this_month = date_today.month
today = date_today.day

emails_to_send = {}

all_birthdays = pandas.read_csv("birthdays.csv")
for (index, birthday) in all_birthdays.iterrows():
    if birthday.month == this_month and birthday.day == today:
        try:
            with open("./letter_templates/birthday_quotes.txt") as quotes_file:
                quotes = quotes_file.readlines()
                quote_to_add = random.choice(quotes).strip()
            with open("./letter_templates/signatures.txt") as signatures_file:
                signatures = signatures_file.readlines()
                signature_to_add = random.choice(signatures).strip()
            with open("./letter_templates/letter_template.txt") as letter_file:
                letter_contents = letter_file.read()
        except FileNotFoundError:
            print("Unable to locate template file(s)...")
        else:
            letter_contents = letter_contents.replace("[RECEIVER_NAME]", birthday.receiver_name)
            letter_contents = letter_contents.replace("[BODY]", quote_to_add)
            letter_contents = letter_contents.replace("[SIGNATURE]", signature_to_add)
            letter_contents = letter_contents.replace("[SENDER_NAME]", SENDER_NAME)

            emails_to_send[birthday.email] = letter_contents

sent = send_emails(emails_to_send)
if len(sent) > 0:
    print(f"Email(s) Sent to: {sent}")
