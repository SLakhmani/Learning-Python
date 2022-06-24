import smtplib
import os
from email.mime.text import MIMEText

SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, results, email_list):
        self.mails_to_send = results
        self.mailing_list = email_list
        self.email_subject = "Low Price Alert!"
        self.email_body = ""
        self.sent_emails = []

    def construct_and_send(self):
        for item in self.mails_to_send:
            if item != "No Results Found":
                mail_text = f"<br>Only £{item.price} to fly from {item.d_city_name}-{item.d_iata_code} " \
                            f"to {item.a_city_name}-{item.a_iata_code},<br>" \
                            f"From {item.outbound_date} to {item.inbound_date}<br>"
                if item.stop_overs >= 1:
                    mail_text += f"Flight has {item.stop_overs} stop over(s) via {', '.join(item.via_cities)}<br>"
                booking_link = f"<a href={item.hyper_link}>Click here to Book</a><br><br>"
                mail_text += booking_link
                self.email_body += mail_text

        if len(self.email_body) > 0:
            self.send_emails()

    def send_emails(self):
        for user in self.mailing_list:
            message_body = MIMEText(f"Hey {user[1]},<br>{self.email_body}", "html")
            email_content = message_body
            email_content['Subject'] = self.email_subject

            try:
                with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
                    connection.starttls()
                    connection.login(SENDER_EMAIL, SENDER_PASSWORD)
                    connection.sendmail(SENDER_EMAIL, user[0], email_content.as_string())
            except:
                print(f"Unable to send email to: {user[0]}")
            else:
                self.sent_emails.append(user[0])

        print(f"Alerts sent to: {self.sent_emails}")
