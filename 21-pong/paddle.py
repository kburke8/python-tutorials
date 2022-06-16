from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_len=5)
        self.goto(x, 0)

    def up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def down(self):
        self.goto(self.xcor(), self.ycor()-20)
