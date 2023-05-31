from turtle import Turtle, Screen

WIDTH = 1000
HEIGHT = 600
BACKGROUND_COLOR = 'black'

def game_screen():
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor(BACKGROUND_COLOR)
    screen.tracer(0)
    return screen
