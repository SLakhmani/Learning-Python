import turtle
import random

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900

screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Welcome to Turtle Racing!")

user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win?"
                                                           "\nPick a color (red, orange, yellow, green, blue, purple): ")
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []

lowest_turtle_pos = -SCREEN_HEIGHT//4

for i in range(len(turtle_colors)):
    t = turtle.Turtle(shape="turtle")
    t.color(turtle_colors[i])
    t.penup()
    t.goto(-(SCREEN_WIDTH // 2) + 10, lowest_turtle_pos + i * 60)
    turtle_list.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > SCREEN_WIDTH//2 - 20:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet.lower():
                print(f"You win! The {winner} turtle was the fastest!")
            else:
                print(f"You Lose! The {winner} turtle was the fastest!")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)
screen.exitonclick()
