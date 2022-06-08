from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 280)
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.write(f"Score:  {self.score}", False, ALIGNMENT, FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score:  {self.score}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write(f"Game Over.", False, ALIGNMENT, FONT)
        self.goto(0, -20)
        self.write(f"Press Enter to go again!", False, ALIGNMENT, FONT)
