from turtle import Turtle
from screen import HEIGHT, WIDTH

COLOR = 'black'
ALIGN = 'center'
FONT = ("Courier", 20, 'bold')

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.print_level()

    def print_level(self, level=1):
        self.penup()
        self.hideturtle()
        self.color(COLOR)
        self.goto(-WIDTH/4, HEIGHT/2 - 50)
        self.pendown()
        self.write(f"LEVEL: {level}", align=ALIGN, font=FONT)

    def update_level(self, level):
        self.clear()
        self.print_level(level)

    def print_game_over(self):        
        self.penup()
        self.home()
        self.write("GAME OVER", align=ALIGN, font=FONT)
    