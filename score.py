from turtle import Turtle, Screen
from screen import HEIGHT, WIDTH

ALIGN = "center"
FONT = ("Courier", 40, 'bold')    
FONT_NAMES = ("Courier", 30, 'bold')    
    
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.cpu_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.write_player_names()
        self.write_score()
        self.draw_net()
    
    def write_player_names(self):
        self.goto(-WIDTH/4, HEIGHT/2 - 50)
        self.write("PLAYER", align=ALIGN, font=FONT_NAMES)
        self.goto(WIDTH/4, HEIGHT/2 - 50)
        self.write("CPU", align=ALIGN, font=FONT_NAMES)

    def write_score(self):
        self.goto(-80, HEIGHT/2 - 60)
        self.write(self.player_score, align=ALIGN, font=FONT)
        self.goto(80, HEIGHT/2 - 60)
        self.write(self.cpu_score, align=ALIGN, font=FONT)

    def update_score(self):
        self.clear()
        self.write_score()

    def draw_net(self):
        self.goto(0, HEIGHT/2 - 5)
        self.setheading(270)
        self.width(5)
        while self.ycor() > -(HEIGHT/2):
            self.pendown()
            self.fd(20)
            self.penup()
            self.fd(20)
        # self.width()
    