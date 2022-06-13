import pandas
import turtle

IMAGE_WIDTH = 725
IMAGE_HEIGHT = 491

# screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
screen.setup(IMAGE_WIDTH, IMAGE_HEIGHT)

# initializing writer turtle
writer = turtle.Turtle()
error_writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
writer.speed("fast")
error_writer.penup()
error_writer.hideturtle()
error_writer.speed("fast")

# importing csv data
states_df = pandas.read_csv("50_states.csv")

game_is_on = True
score = 0
guessed_states = []
total_states = states_df.state.count()

while game_is_on:
    if score < total_states:
        user_input = turtle.textinput(f"States Guessed: {score}/{total_states}", "Enter name of state:")
        error_writer.clear()
        if user_input is not None:
            user_input = user_input.title()
            row = states_df[states_df.state == user_input]
            if not row.empty:
                if user_input in guessed_states:
                    error_writer.goto(0, IMAGE_HEIGHT // 2 - 25)
                    error_writer.color("green")
                    error_writer.write("You guessed that already!", align="center", font=('Courier', 15, 'bold'))
                else:
                    score += 1
                    writer.goto(float(row.x), float(row.y))
                    writer.write(user_input)
                    guessed_states.append(user_input)
            else:
                error_writer.goto(0, IMAGE_HEIGHT//2 - 25)
                error_writer.color("red")
                error_writer.write("State does not exist!", align="center", font=('Courier', 15, 'bold'))
        else:
            writer.goto(0, 0)
            writer.color("red")
            writer.write(f"Final Score: {score}/{total_states}", align="center", font=('Courier', 20, 'bold'))
            game_is_on = False
    else:
        writer.goto(0, 0)
        writer.color("green")
        writer.write(f"You got em all!", align="center", font=('Courier', 20, 'bold'))
        game_is_on = False

turtle.mainloop()
