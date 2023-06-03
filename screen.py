from turtle import Screen

WIDTH = 1000
HEIGHT = 600
BACKGROUND_COLOR = 'black'

def game_screen():
    screen = Screen()    
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor(BACKGROUND_COLOR)
    screen.tracer(0)

    return screen


def number_of_players(screen):
    number_of_players =screen.numinput(
        title="Pong Game",
        prompt="How many players?",
        default=1,
        minval=1,
        maxval=2)
    if number_of_players == None:
        return 1
    else:
        return number_of_players
