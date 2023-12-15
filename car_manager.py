from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        prob = random.randint(1, 6)
        if prob == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            rand_y = random.randint(-250, 250)
            new_car.goto(300, rand_y)
            self.all_cars.append(new_car)

    def move_along_x(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def inc_car_speed(self):
        self.car_speed += MOVE_INCREMENT



