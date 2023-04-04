from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.move_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_spawn = random.randint(1, 6)
        if random_spawn == 1:
            new_car = Turtle("square")
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-260, 260)
            new_car.goto(400, random_y)
            self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            new_x = car.xcor() - self.move_speed
            car.goto(new_x, car.ycor())

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT


