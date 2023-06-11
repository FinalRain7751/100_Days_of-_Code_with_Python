from turtle import Turtle, Screen
from player import Player
from screen import game_screen, HEIGHT, WIDTH
from level import Level
from traffic import Traffic
import time

screen = game_screen()
player = Player()
cars = Traffic()

current_level = 1
level = Level()

is_game_on = True
speed = 0.1

screen.update()

screen.listen()
screen.onkeypress(player.move_fd, key='Up')

def is_collision(cars):
    for car in cars:
        if car.distance(player) < 20:
            return True
    return False


while is_game_on:
    cars.generate_traffic()
    cars.move_traffic()
    if player.ycor() > HEIGHT/2 - 20:
        player.reset()
        current_level += 1
        level.update_level(current_level)
        cars.increase_speed()

    if is_collision(cars.traffic):
        level.print_game_over()
        cars.clear_traffic()
        is_game_on = False

    cars.remove_passed_cars()   

    time.sleep(speed)
    screen.update()
    

screen.exitonclick()