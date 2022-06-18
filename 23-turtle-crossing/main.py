import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    manager.generate_cars()
    manager.move_cars()
    if not manager.check_player_position(player):
        player.reset()
        scoreboard.reset()
    if player.at_finish_line():
        scoreboard.score()
        player.reset()
        manager.speed_up()




screen.exitonclick()

