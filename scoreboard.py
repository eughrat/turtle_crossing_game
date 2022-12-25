from turtle import Turtle


ALIGMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-245, 275)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 15, "normal"))

    def level_up(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
        self.speed() + 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGMENT,font=FONT)