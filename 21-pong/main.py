from turtle import Screen, Turtle
from paddle import Paddle

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

screen.listen()
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
