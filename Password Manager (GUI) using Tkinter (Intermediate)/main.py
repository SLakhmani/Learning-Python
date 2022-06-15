from random import choices, shuffle, randint
from tkinter import *
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    num_alpha = randint(4, 8)
    num_symbols = randint(2, 4)
    num_numbers = randint(2, 4)

    password_list = []
    password_list.extend(choices(letters, weights=None, cum_weights=None, k=num_alpha))
    password_list.extend(choices(symbols, weights=None, cum_weights=None, k=num_symbols))
    password_list.extend(choices(numbers, weights=None, cum_weights=None, k=num_numbers))
    shuffle(password_list)
    password = ''.join(password_list)

    return password


# ---------------------------- BUTTON EVENTS ------------------------------- #
def generate_password_button():
    password = generate_password()
    password_box.delete(0, END)
    password_box.insert(END, string=password)
    pyperclip.copy(password)


def add_password_button():
    if len(website_box.get()) != 0 and len(email_box.get()) != 0 and len(password_box.get()) != 0:
        save_password()
        website_box.delete(0, END)
        password_box.delete(0, END)
        messagebox.showinfo(title="Success", message="Password Saved and Copied to clipboard!")
    else:
        messagebox.showerror(title="Oops!", message="Cannot leave fields empty!")


def search_button():
    key = website_box.get()
    try:
        with open("saved_passwords.json", "r") as pwd_file:
            entries = json.load(pwd_file)
    except FileNotFoundError:
        messagebox.showerror(title="Oops!", message="Could not locate password file!")
    else:
        if key in entries:
            email_username = entries[key]["email/username"]
            password = entries[key]["password"]
            messagebox.showinfo(title=f"{key}", message=f"Email/Username: {email_username}\nPassword: {password}")
            pyperclip.copy(password)
        else:
            messagebox.showerror(title="Oops!", message=f"Could not find any entry for {key}!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    new_entry = {
        website_box.get(): {
            "email/username": email_box.get(),
            "password": password_box.get(),
        }
    }
    try:
        with open("saved_passwords.json", "r") as pwd_file:
            entry = json.load(pwd_file)
            entry.update(new_entry)
    except FileNotFoundError:
        with open("saved_passwords.json", "w") as pwd_file:
            json.dump(new_entry, pwd_file, indent=4)
    else:
        with open("saved_passwords.json", "w") as pwd_file:
            json.dump(entry, pwd_file, indent=4)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.config(width=300, height=300, padx=20, pady=20)
window.title("Password Manager")

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")  # Logo
canvas.create_image(100, 95, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0, sticky=E)

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0, sticky=E)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0, sticky=E)

# Text Boxes
website_box = Entry(width=30)
website_box.grid(column=1, row=1, sticky=W + E, pady=5)

email_box = Entry(width=35)
email_box.grid(column=1, row=2, columnspan=2, sticky=W + N + S + E, pady=5)

password_box = Entry(width=30)
password_box.grid(column=1, row=3, sticky=W + E, pady=5)

# Buttons
search_button = Button(text="Search", command=search_button)
search_button.grid(column=2, row=1, padx=5, sticky=W + E)

generate_button = Button(text="Generate Password", command=generate_password_button)
generate_button.grid(column=2, row=3, padx=5, sticky=W + E)

add_button = Button(text="Save Password", width=30, command=add_password_button)
add_button.grid(column=1, row=4, columnspan=2, sticky=W + N + S + E)

window.mainloop()
