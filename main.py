import time
from turtle import Screen
import random

from car_manager import Car
from player import Player
from scoreboard import ScoreBoard

START_POSITION = (300, random.randint(-250,250))

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
cars = Car()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")

loop = 0
game_is_on = True
while game_is_on:
    loop += 1
    screen.update()
    screen.update()
    time.sleep(0.1)
    cars.create_cars()
    cars.move_car()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 280:
        player.reset_position()
        scoreboard.level_up()



screen.exitonclick()