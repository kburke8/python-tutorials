from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 280)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, 'center', ("Arial", 14, "normal"))

    def increase_score(self):
        self.score += 1
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 14, "normal"))
