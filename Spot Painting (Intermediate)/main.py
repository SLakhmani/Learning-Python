import turtle
import random

turtle_obj = turtle.Turtle()
dot_width = 20
spacing = 50
columns = 10
rows = 10

# list of random colors to use
color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83),
              (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47),
              (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151)]

turtle_obj.speed("fastest")
turtle.colormode(255)

# setting initial positions
turtle_obj.hideturtle()
turtle_obj.up()
turtle_obj.back(200)
turtle_obj.setheading(270)
turtle_obj.forward(200)
turtle_obj.setheading(0)

# new origin coordinates
origin_x = turtle_obj.xcor()
origin_y = turtle_obj.ycor()

# printing the pattern
for i in range(rows):
    turtle_obj.down()
    for _ in range(columns):
        turtle_obj.color(random.choice(color_list))
        turtle_obj.dot(dot_width)
        turtle_obj.up()
        turtle_obj.forward(spacing)
        turtle_obj.down()
    turtle_obj.up()
    turtle_obj.setpos(origin_x, origin_y + (i + 1) * spacing)

screen = turtle.Screen()
screen.exitonclick()
