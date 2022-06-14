import random
from tkinter import *

NUM_ALPHA = 8
NUM_SYMBOLS = 4
NUM_NUMBERS = 4


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Initialize character lists
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list.extend(random.choices(letters, weights=None, cum_weights=None, k=NUM_ALPHA))
    password_list.extend(random.choices(symbols, weights=None, cum_weights=None, k=NUM_SYMBOLS))
    password_list.extend(random.choices(numbers, weights=None, cum_weights=None, k=NUM_NUMBERS))
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password


# ---------------------------- BUTTON EVENTS ------------------------------- #
def generate_password_button():
    password = generate_password()
    password_box.delete(0, END)
    password_box.insert(END, string=password)


def add_password_button():
    save_password()
    website_box.delete(0, END)
    email_box.delete(0, END)
    password_box.delete(0, END)
    show_confirmation(3)


def show_confirmation(confirmation_timer):
    confirmation_label.config(foreground="green")
    if confirmation_timer > 0:
        window.after(1000, show_confirmation, confirmation_timer - 1)
    else:
        confirmation_label.config(foreground="white")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    try:
        with open("saved_passwords.txt", "a") as pwd_file:
            pwd_file.write(f"Website: {website_box.get()} | Email/Username: {email_box.get()} "
                           f"| Password: {password_box.get()}\n")
    except OSError as err:
        raise OSError(err)
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise


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

confirmation_label = Label(text="Password Saved!", foreground="white", font=("Arial", 15, "bold"))
confirmation_label.grid(row=0, column=2)

# Text Boxes
website_box = Entry(width=35)
website_box.grid(column=1, row=1, columnspan=2, sticky=W + N + S + E, pady=10)

email_box = Entry(width=35)
email_box.grid(column=1, row=2, columnspan=2, sticky=W + N + S + E, pady=10)

password_box = Entry(width=30)
password_box.grid(column=1, row=3, sticky=W + E, pady=10)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password_button)
generate_button.grid(column=2, row=3, padx=5, sticky=W + E)

add_button = Button(text="Save Password", width=30, command=add_password_button)
add_button.grid(column=1, row=4, columnspan=2, sticky=W + N + S + E)

window.mainloop()
