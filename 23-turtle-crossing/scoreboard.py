from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 230)
        self.level = 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Level: {self.level}", False, 'center', FONT)

    def score(self):
        self.level += 1
        self.display_score()

    def reset(self):
        self.level = 1
        self.display_score()
