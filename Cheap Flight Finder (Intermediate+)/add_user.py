import os
import requests

users_endpoint = os.environ['USERS_ENDPOINT']

email_correct = False

print("Welcome to Lakhmani's Flight Club!")
print("We find the best flight deals and email you.\n")
first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")

while not email_correct:
    email_correct = True
    email = input("Enter your email: ")
    email_confirm = input("Re-enter your email to confirm: ")
    
    if email == email_confirm:
        email_correct = True
        user_data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
        }
        
        response = requests.post(users_endpoint, json=user_data)
        response.raise_for_status()
        print("You've been added to the flight club!")
    else:
        print("\nPlease make sure you enter the correct Email.\n")
