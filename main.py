import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.new_car()
    car_manager.move_along_x()

    # detect turtle touching the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
            scoreboard.game_over()

    # detect successful lap
    if player.at_finish():
        player.initial_pos()
        car_manager.inc_car_speed()
        scoreboard.inc_level()

screen.exitonclick()


