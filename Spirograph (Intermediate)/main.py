from turtle import Turtle, Screen
import random


def change_color():
    r = random.random()
    b = random.random()
    g = random.random()

    return r, g, b


turtle_obj = Turtle()

heading = turtle_obj.heading()
circle_radius = 100
heading_angle = 5

turtle_obj.speed("fastest")
for _ in range(360//heading_angle):
    turtle_obj.color(change_color())
    turtle_obj.circle(circle_radius)
    heading += heading_angle
    turtle_obj.setheading(heading)

screen = Screen()
screen.exitonclick()
