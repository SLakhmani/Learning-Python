from tkinter import *
from quiz_brain import QuizBrain

BG_COLOR = "#4CACBC"
CANVAS_COLOR = "#FCF8E8"
TEXT_COLOR = "#06283D"
WRONG_COLOR = "#F47C7C"
RIGHT_COLOR = "#A0D995"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.is_correct = False
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler: True or False")
        self.window.config(padx=25, pady=25, bg=BG_COLOR)

        self.score_label = Label(text="Score: 0", foreground="white", bg=BG_COLOR, font=("Arial", 12, "bold"))
        self.score_label.grid(row=0, column=1, sticky=E)

        self.canvas = Canvas(height=250, width=300, highlightthickness=0, bg=CANVAS_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=270,
            text="Sample Text",
            font=("Arial", 16, "italic"),
            fill=TEXT_COLOR)

        true_photo = PhotoImage(file="./images/true.png")
        false_photo = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=true_photo, highlightthickness=0, command=self.true_button_click)
        self.false_button = Button(image=false_photo, highlightthickness=0, command=self.false_button_click)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=CANVAS_COLOR)
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've Reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button_click(self):
        self.is_correct = self.quiz.check_answer("True")
        self.update_score_text(self.is_correct)

    def false_button_click(self):
        self.is_correct = self.quiz.check_answer("False")
        self.update_score_text(self.is_correct)

    def update_score_text(self, is_correct):
        if is_correct is True:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg=RIGHT_COLOR)
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg=WRONG_COLOR)
            self.window.after(1000, self.get_next_question)

