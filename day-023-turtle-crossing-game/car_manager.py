import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self, pos_x, pos_y, shape="square"):
        super().__init__(shape)
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.goto(pos_x, pos_y)
        self.move_distance = STARTING_MOVE_DISTANCE


class CarManager:
    def __init__(self):
        self.cars = []

    def spawn_car(self):
        random_y = random.randint(-250, 250)
        self.cars.append(Car(300, random_y))

    def move_cars(self):
        for car in self.cars:
            new_x = car.xcor() - car.move_distance
            car.goto(new_x, car.ycor())

    def accelarate_cars(self):
        for car in self.cars:
            car.move_distance += MOVE_INCREMENT

    def all_cars(self):
        return self.cars
