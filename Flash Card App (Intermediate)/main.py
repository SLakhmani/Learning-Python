from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TIMER = None
CURRENT_RECORD = {}
CARD_FLIP_DELAY = 3000  # milliseconds
# ------------------ LANGUAGE DATA ------------------ #
try:
    language_data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    language_data = pandas.read_csv("./data/french_words.csv")
    to_learn = language_data.to_dict(orient="records")
except pandas.errors.EmptyDataError:
    language_data = pandas.read_csv("./data/french_words.csv")
    to_learn = language_data.to_dict(orient="records")
else:
    to_learn = language_data.to_dict(orient="records")


# ------------------ GENERATE WORD ------------------ #
def next_word():
    global TIMER, CURRENT_RECORD
    window.after_cancel(TIMER)
    CURRENT_RECORD = random.choice(to_learn)
    canvas.itemconfig(display_image, image=card_front_image)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=CURRENT_RECORD["French"], fill="black")
    TIMER = window.after(CARD_FLIP_DELAY, flip_card)


# ------------------ WORD KNOWN BUTTON PRESS ------------------ #
def check_button_press():
    to_learn.remove(CURRENT_RECORD)
    if len(to_learn) == 0:
        messagebox.showinfo(title="Congratulations!", message="You have learnt all the words in the dictionary!\n"
                                                              "How about a Revision?")
        reset_to_learn()
    else:
        to_learn_dataframe = pandas.DataFrame(to_learn)
        to_learn_dataframe.to_csv("./data/words_to_learn.csv", index=False)
    next_word()


# ------------------ RESET DICTIONARY IF ALL WORDS GUESSED ------------------ #
def reset_to_learn():
    global language_data, to_learn
    language_data = pandas.read_csv("./data/french_words.csv")
    to_learn = language_data.to_dict(orient="records")


# ------------------ FLIP CARD ------------------ #
def flip_card():
    canvas.itemconfig(display_image, image=card_back_image)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=CURRENT_RECORD["English"], fill="white")


# ------------------ UI SETUP ------------------ #
# Window
window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.title("Flash Card App")

TIMER = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=530, highlightthickness=0, background=BACKGROUND_COLOR)
card_back_image = PhotoImage(file="./images/card_back.png")
card_front_image = PhotoImage(file="./images/card_front.png")

display_image = canvas.create_image(400, 265, image=card_front_image)
language_text = canvas.create_text(400, 150, text="Language", font=("Arial", 35, "italic"))
word_text = canvas.create_text(400, 255, text="Word", font=("Arial", 55, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
check_image = PhotoImage(file="./images/right.png")
cross_image = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, border=0, command=next_word)
cross_button.grid(row=1, column=0)
check_button = Button(image=check_image, highlightthickness=0, border=0, command=check_button_press)
check_button.grid(row=1, column=1)

next_word()
window.mainloop()
