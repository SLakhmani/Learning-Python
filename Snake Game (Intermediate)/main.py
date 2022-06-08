from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def continue_game():
    screen = Screen()
    screen.clear()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    game_is_on = True

    snake = Snake()
    food = Food()
    score = Scoreboard()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(continue_game, "Return")
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.update_score()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            score.game_over()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                score.game_over()

    screen.exitonclick()


continue_game()
