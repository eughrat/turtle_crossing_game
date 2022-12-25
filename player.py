from turtle import Turtle


START_POSITION = (0,-280)

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.start_position = START_POSITION
        self.create_player()


    def create_player(self):
        self.penup()
        self.left(90)
        self.color("black")
        self.shape("turtle")
        self.goto(self.start_position)

    def go_up(self):
        new_y = self.ycor() +20
        self.goto(self.xcor(), new_y)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
