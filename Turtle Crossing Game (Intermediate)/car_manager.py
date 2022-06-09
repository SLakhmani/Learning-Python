from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_START_POS = 260


class CarManager(Turtle):
    def __init__(self, level):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.penup()
        self.color(random.choice(COLORS))
        self.move_speed = STARTING_MOVE_DISTANCE + (level - 1) * MOVE_INCREMENT
        random_y_cor = random.randint(-250, 250)
        self.goto(CAR_START_POS, random_y_cor)

    def move(self):
        self.goto(self.xcor() - self.move_speed, self.ycor())
