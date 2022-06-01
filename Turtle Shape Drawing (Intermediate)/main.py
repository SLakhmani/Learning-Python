from turtle import Turtle,  Screen
import random


def update_angle(sides):
    return 360 / sides


def change_color():
    r = random.random()
    b = random.random()
    g = random.random()

    return r, g, b


timmy = Turtle()
SIDE = 100
num_sides = 3
num_shapes = 8

for _ in range(num_shapes):
    turn = update_angle(num_sides)
    timmy.color(change_color())
    for _ in range(num_sides):
        timmy.forward(SIDE)
        timmy.right(turn)
    num_sides += 1

screen = Screen()
screen.exitonclick()
