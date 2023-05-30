from turtle import Turtle
from random import randrange, choice

COLORS = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.modify_food()

    def new_pos(self):
        x = randrange(-280, 280, 20)
        y = randrange(-280, 280, 20)
        return x, y
    
    def modify_food(self):  
        self.resizemode('user')
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('limegreen')
        self.hideturtle()
        self.penup()
        self.goto(self.new_pos())
        self.showturtle()

    def move_food(self):
        self.color(choice(COLORS))
        self.goto(self.new_pos())
