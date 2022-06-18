from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = 1

    def generate_cars(self):
        if random.randint(1, 100) > 80:
            self.create_car()

    def create_car(self):
        car = Turtle()
        car.penup()
        car.goto(300, random.randint(-230, 270))
        car.color(random.choice(COLORS))
        car.shape('square')
        car.shapesize(stretch_wid=1, stretch_len=2)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.goto(car.xcor() - MOVE_INCREMENT * self.speed, car.ycor())
            if car.xcor() < -300:
                car.clear()
                self.cars.remove(car)

    def check_player_position(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return False
        return True

    def speed_up(self):
        self.speed += .1
