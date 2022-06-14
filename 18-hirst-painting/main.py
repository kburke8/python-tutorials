import turtle as turtle_module
import random


def turn(direction, distance):
    if direction == 'left':
        turt.left(90)
        turt.forward(distance)
        turt.left(90)
        turt.forward(distance)
    elif direction == 'right':
        turt.right(90)
        turt.forward(distance)
        turt.right(90)
        turt.forward(distance)


def print_row(row_count):
    for _ in range(row_count):
        turt.dot(20, random.choice(color_list))
        turt.forward(DISTANCE)


color_list = [(202, 164, 110), (240, 245, 241), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

DISTANCE = 50


turt = turtle_module.Turtle()
turt.penup()
turt.hideturtle()
turtle_module.colormode(255)

turt.setheading(135)
turt.forward(450)
turt.setheading(0
                )
for y in range(10):
    print_row(10)
    if y % 2 == 0:
        turn('right', DISTANCE)
    else:
        turn('left', DISTANCE)

screen = turtle_module.Screen()
screen.exitonclick()
