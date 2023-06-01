from turtle import Turtle
from screen import HEIGHT
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.resizemode("user")
        self.shape('circle')
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("white")
        self.penup()
        
    def ball_starts_moving(self):
        self.setheading(270)
        self.fd(2)
    
    def ball_set_initial_direction(self):     
        self.setheading(randint(135, 180))
        
        
    def ball_moving(self):
        self.fd(2)
        