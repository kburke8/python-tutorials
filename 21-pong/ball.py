from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.width = 20
        self.penup()
        self.shape('circle')
        self.color("white")
        self.ball_speed = 1
        self.x_move = 10
        self.y_move = 10

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.ball_speed = 1

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 1.05

    def move(self):
        current_x = self.xcor()
        current_y = self.ycor()

        if current_y > 280 or current_y < -280:
            self.bounce_y()

        new_y = current_y + self.y_move * self.ball_speed
        new_x = current_x + self.x_move * self.ball_speed

        self.goto(new_x, new_y)
