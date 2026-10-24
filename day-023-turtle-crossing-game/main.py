import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_player, "Up")

spawn_timer = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    spawn_timer += 1

    if spawn_timer % 6 == 0:
        car_manager.spawn_car()

    for car in car_manager.all_cars():
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 250:
        scoreboard.increase_level()
        scoreboard.update_scoreboard()
        car_manager.accelarate_cars()
        player.reset_position()

screen.exitonclick()
