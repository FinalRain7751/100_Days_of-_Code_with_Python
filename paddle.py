from turtle import Turtle

from screen import HEIGHT, WIDTH

class Paddle():
    def __init__(self):
        self.player_paddles = []
        self.cpu_paddles = []
        self.player_paddle = self.create_paddle("player")
        self.cpu_paddle = self.create_paddle("cpu")

    def create_paddle(self, user="cpu"):
        if user == "player":
            x = -(WIDTH/2 - 20)
        else:
            x = WIDTH/2 - 25

        for i in range(3):
            paddle_unit = Turtle()
            paddle_unit.resizemode("user")
            paddle_unit.shape("square")
            paddle_unit.color("white")
            paddle_unit.penup()
            paddle_unit.goto(x, 20-i*20)

            if user == "player":
                self.player_paddles.append(paddle_unit)
            else:
                self.cpu_paddles.append(paddle_unit)
                

    def move_player_paddle_up(self):
        self.move_paddle(90, "player")
    
    def move_player_paddle_down(self):
        self.move_paddle(270, "player")
    
    def move_cpu_paddle_up(self):
        self.move_paddle(90)
    
    def move_cpu_paddle_down(self):
        self.move_paddle(270)

    def move_paddle(self, direction, user="cpu"):
        max_y = HEIGHT/2 - 20  
        min_y = -(HEIGHT/2 -20)

        if user == "player":
            paddles = self.player_paddles
        else:
            paddles = self.cpu_paddles
        
        if direction == 90:
            head = paddles[0] 
        else:
            head = paddles[-1]

        if (head.ycor() < max_y and head.ycor() > min_y):
            for i in range(len(paddles)):
                paddle_unit = paddles[i]
                paddle_unit.setheading(direction)
                paddle_unit.fd(20)
                


        


