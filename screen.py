from turtle import Screen, Turtle

HEIGHT = 600
WIDTH = 800
BACKGROUND_COLOR = 'white'


def game_screen():
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor(BACKGROUND_COLOR)
    screen.tracer(0)
    return screen


