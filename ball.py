from turtle import Turtle
from screen import HEIGHT
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = 5
        self.resizemode("user")
        self.shape('circle')
        self.color("white")
        self.penup()

    def starts_moving(self):
        self.setheading(self.set_initial_direction())
        self.fd(4)
    
    def set_initial_direction(self): 
        while True:
            angle = randint(110, 250) 
            if not angle in range(160, 180):   
                return angle        
        
    def moving(self):
        self.fd(self.speed)

    def set_return_direction(self):
        hitting_angle = self.heading()
        return_angle = 180 - hitting_angle
        if return_angle < 0:
            return_angle += 360
        return return_angle
        
    def is_hitting_paddle(self, paddles):
        for i in range(len(paddles)):
            if self.distance(paddles[i]) < 20:  
                self.setheading(self.set_return_direction())  
                return True
        return False            
            
    def is_hitting_wall(self):
        is_hitting_wall = self.ycor() > HEIGHT/2 - 15 or self.ycor() < -(HEIGHT/2 -15)
        if is_hitting_wall:
            self.setheading(360 - self.heading())
    