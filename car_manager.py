from turtle import Turtle
import random

COLORS = ['red', 'green', 'blue', 'yellow', 'pink', 'violet', 'black']

START_POSITION = (300, random.randint(-250,250))

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.left(180)
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2.5)
        self.x_move = -10
        self.goto(START_POSITION)
        self.move()


    def move(self):
        newx = self.xcor() + self.x_move
        self.goto(newx, self.ycor())

    def reset_position(self):
        self.goto(START_POSITION)
