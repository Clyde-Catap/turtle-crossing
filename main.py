import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random


CARS_GARAGE = []



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()


score = Scoreboard()

ending = Scoreboard()


screen.listen()
screen.onkeypress(player.move, "Up")


def carspawn(x):
    car_number = random.randint(1,x)
    for cars in range(car_number):
        y_location = random.randrange(start=-240, stop=280, step=20)
        kotse = CarManager()
        kotse.goto(290, y_location)
        CARS_GARAGE.append(kotse)



difficulty = 6
level = 1
multiplier_speed = 0.1
car_number = 4

game_is_on = True

# def restarter():
while game_is_on:
    time.sleep(multiplier_speed)
    screen.update()
    skipper = random.randint(1, 6)
    score.writee(level)
#difficulty increase
    if player.ycor() > 300:
        score.clear()
        level += 1
        player.setpos(x=0, y=-280)
        multiplier_speed *= 0.5
        car_number += 1
        difficulty -= 1

    if difficulty < 0:
        ending.game_over("You WIN")

    for vrrom in CARS_GARAGE:
        vrrom.move()
        if vrrom.distance(player) < 20:
            game_is_on = False
            ending.game_over("Game Over")
    if skipper%difficulty == 0:
        pass
        carspawn(car_number)
        # restarter()


# COLLISION OCTOBER 16, 2022

# restarter()
screen.exitonclick()