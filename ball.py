from turtle import Turtle
from screen import HEIGHT, WIDTH
from random import randint, choice

INITIAL_SPEED = 5

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = INITIAL_SPEED
        self.resizemode("user")
        self.shape('circle')
        self.color("white")
        self.penup()

    def starts_moving(self, winner):
        self.setheading(self.set_initial_direction(winner))
    
    def set_initial_direction(self, winner): 
        if winner == "cpu" or winner == "player2":
            while True:
                angle = randint(110, 250) 
                if not angle in range(160, 180):   
                    return angle        
        else:
            while True:
                angle1 = randint(20, 70)
                angle2 = randint(290, 340)
                return choice([angle1, angle2])       
                
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
                self.fd(10)
                return True
        return False            
            
    def is_hitting_wall(self):
        is_hitting_wall = self.ycor() > HEIGHT/2 - 15 or self.ycor() < -(HEIGHT/2 -15)
        if is_hitting_wall:
            self.setheading(360 - self.heading())
    