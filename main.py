import time
from turtle import Screen

from car_manager import Car
from player import Player
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
scoreboard = ScoreBoard()
car1 = Car()
car2 = Car()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    if player.ycor() > 280:
        player.reset_position()
        scoreboard.level_up()



screen.exitonclick()