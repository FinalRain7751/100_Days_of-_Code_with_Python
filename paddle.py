from turtle import Turtle
import math

from screen import HEIGHT, WIDTH

MAX_Y = HEIGHT/2 - 20  
MIN_Y = -(HEIGHT/2 -20)
PADDLE_UNITS = 5

class Paddle():
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.player1_paddles = []
        self.player1_paddle = self.create_paddle("player1")
        if self.number_of_players == 1:
            self.cpu_paddles = []
            self.cpu_paddle = self.create_paddle("cpu")
        elif self.number_of_players == 2: 
            self.player2_paddles = []
            self.player2_paddle = self.create_paddle("player2")

    def create_paddle(self, user="cpu"):
        if user == "player1":
            x = -(WIDTH/2 - 20)
        else:
            x = WIDTH/2 - 25

        for i in range(PADDLE_UNITS):
            paddle_unit = Turtle()
            paddle_unit.resizemode("user")
            paddle_unit.shape("square")
            paddle_unit.color("white")
            paddle_unit.penup()
            paddle_unit.goto(x, (20*(PADDLE_UNITS-1)/2)-i*20)

            if user == "player1":
                self.player1_paddles.append(paddle_unit)
            elif user == "player2":
                self.player2_paddles.append(paddle_unit)
            else:
                self.cpu_paddles.append(paddle_unit)
                

    def move_player1_paddle_up(self):
        self.move_paddle(90, "player1")
    
    def move_player1_paddle_down(self):
        self.move_paddle(270, "player1")

    def move_player2_paddle_up(self):
        self.move_paddle(90, "player2")
    
    def move_player2_paddle_down(self):
        self.move_paddle(270, "player2")
    
    def move_cpu_paddle_up(self):
        self.move_paddle(90)
    
    def move_cpu_paddle_down(self):
        self.move_paddle(270)

    def move_paddle(self, direction, user="cpu"):
        if user == "player1":
            paddles = self.player1_paddles
            paddle_speed = 20

        elif user == "player2":
            paddles = self.player2_paddles
            paddle_speed = 20

        else:
            paddles = self.cpu_paddles
            paddle_speed = 10
        
        if direction == 90:
            head = paddles[0] 
        else:
            head = paddles[-1]

        if (head.ycor() < MAX_Y and head.ycor() > MIN_Y):
            for i in range(len(paddles)):
                paddle_unit = paddles[i]
                paddle_unit.setheading(direction)
                paddle_unit.fd(paddle_speed)

    def move_cpu_paddle(self, ball):
        paddle_ycor = self.cpu_paddles[1].ycor()
        ball_angle = ball.heading()
        if ball_angle > 90:
            ball_angle = 360 - ball_angle

        if ball.xcor() > 0:
            ball_x = (WIDTH/2 - 25) - ball.xcor()
            ball_y = ball.ycor()
            ball_projected_y = ball_x*math.tan(ball_angle)
            if ball_angle > 90:
                ball_projected_ycor = ball_y - ball_projected_y
            else:
                ball_projected_ycor = ball_y + ball_projected_y 

            if -5 > paddle_ycor - ball_projected_ycor > 5:
                for i in range(3):
                    self.cpu_paddles[i].goto(WIDTH/2 - 25, ball_projected_ycor+(20*(PADDLE_UNITS-1)/2)-i*20)
            elif ball_projected_ycor > paddle_ycor:
                self.move_cpu_paddle_up()
            elif ball_projected_ycor < paddle_ycor:
                self.move_cpu_paddle_down()
            
        else:
            if -5 > paddle_ycor > 5:
                for i in range(3):
                    self.cpu_paddles[i].goto(WIDTH/2 - 25, (20*(PADDLE_UNITS-1)/2)-i*20)
            elif paddle_ycor < 0:
                self.move_cpu_paddle_up()
            elif paddle_ycor > 0:
                self.move_cpu_paddle_down()
             

    def reset_position(self):
        self.go_home(self.player1_paddles)
        if self.number_of_players == 2:
            self.go_home(self.player2_paddles)
        elif self.number_of_players == 1:
            self.go_home(self.cpu_paddles)

    def go_home(self, paddles):
        for i in range(PADDLE_UNITS):
            paddles[i].sety((20*(PADDLE_UNITS-1)/2)-(i*20))



                


        


