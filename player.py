from turtle import Turtle
from screen import HEIGHT, WIDTH

STARTING_POS = (0, -HEIGHT/2 + 20)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POS)

    def move_fd(self):
        self.fd(20)

    def reset(self):
        self.goto(STARTING_POS)