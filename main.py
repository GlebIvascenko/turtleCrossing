import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "space")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()

    #next level
    if player.ycor() > 280:
        player.next_level()
        scoreboard.increase_level()
        car.increase_speed()

    for each_car in car.car_list:
        if each_car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()




screen.exitonclick()