from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.resizemode("user")
        self.shape('circle')
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("white")
        self.penup()
        
    
        