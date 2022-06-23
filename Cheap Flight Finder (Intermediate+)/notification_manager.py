import smtplib
import os

SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")
RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, results):
        self.mails_to_send = results
        self.email_subject = "Subject:Low Price Alert!\n\n"
        self.email_body = ""

    def construct_and_send(self):
        for item in self.mails_to_send:
            if item != "No Results Found":
                mail_text = f"Only £{item.price} to fly from {item.d_city_name}-{item.d_iata_code} " \
                            f"to {item.a_city_name}-{item.a_iata_code},\n" \
                            f"From {item.outbound_date} to {item.inbound_date}\n\n"
                self.email_body += mail_text

        if len(self.email_body) > 0:
            return self.send_email()
        else:
            return False

    def send_email(self):
        message_body = f"{self.email_subject}{self.email_body}"

        try:
            with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
                connection.starttls()
                connection.login(SENDER_EMAIL, SENDER_PASSWORD)
                connection.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message_body.encode("utf-8"))
        except:
            print(f"Unable to send email to: {RECEIVER_EMAIL}")
        else:
            return True
