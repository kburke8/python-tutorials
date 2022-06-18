from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


LEFT = -350
RIGHT = 350

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)
# screen.tracer(0)

left_paddle = Paddle(LEFT)
right_paddle = Paddle(RIGHT)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')

game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    ball.move()
    if (ball.xcor() > 320 and ball.distance(right_paddle) < 40)\
            or (ball.xcor() < -320 and ball.distance(left_paddle) < 40):
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset()
    elif ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset()

screen.exitonclick()
