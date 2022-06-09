import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

new_player = Player()
score = Scoreboard()
cars = []

screen.listen()
screen.onkey(new_player.go_up, "Up")
screen.onkey(new_player.go_down, "Down")

counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if new_player.is_at_finish_line():
        for car in cars:
            car.hideturtle()
            car.clear()
        score.increase_level()
        new_player.new_level()
        cars.clear()
        counter = 0

    if counter % 6 == 0:
        car = CarManager(score.level)
        cars.append(car)

    for car in cars:
        car.move()
        if car.distance(new_player) < 20:
            game_is_on = False
            score.game_over()
        if car.xcor() < -340:
            car.clear()
            cars.remove(car)

    counter += 1

screen.exitonclick()
