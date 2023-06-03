from turtle import Turtle, Screen
from screen import HEIGHT, WIDTH

ALIGN = "center"
FONT = ("Courier", 40, 'bold')    
FONT_NAMES = ("Courier", 30, 'bold')   
INCREASE_SPEED_AFTER = 2 
    
class Scoreboard(Turtle):
    def __init__(self, number_of_players):
        super().__init__()
        self.number_of_players = number_of_players
        self.player1_score = 0
        if self.number_of_players == 2:
            self.player2_score = 0
        elif self.number_of_players == 1:
            self.cpu_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.write_player_names()
        self.write_score()
        self.draw_net()
    
    def write_player_names(self):
        self.goto(-WIDTH/4, HEIGHT/2 - 50)
        self.write("PLAYER 1", align=ALIGN, font=FONT_NAMES)
        self.goto(WIDTH/4, HEIGHT/2 - 50)
        if self.number_of_players == 1:
            self.write("CPU", align=ALIGN, font=FONT_NAMES)
        elif self.number_of_players == 2:
            self.write("PLAYER 2", align=ALIGN, font=FONT_NAMES)

    def write_score(self):
        self.goto(-80, HEIGHT/2 - 60)
        self.write(self.player1_score, align=ALIGN, font=FONT)
        self.goto(80, HEIGHT/2 - 60)
        if self.number_of_players == 2:
            self.write(self.player2_score, align=ALIGN, font=FONT)
        elif self.number_of_players == 1:
            self.write(self.cpu_score, align=ALIGN, font=FONT)

    def draw_net(self):
        self.goto(0, HEIGHT/2 - 5)
        self.setheading(270)
        self.width(5)
        while self.ycor() > -(HEIGHT/2):
            self.pendown()
            self.fd(20)
            self.penup()
            self.fd(20)
    
    def update_score(self):
        self.clear()
        self.write_player_names()
        self.write_score()
        self.draw_net()

