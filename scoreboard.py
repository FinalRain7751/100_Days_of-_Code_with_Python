from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 14, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color('white')
        self.draw_scoreboard()
    
    def update_score(self):
        self.score += 1
        self.draw_scoreboard()

    def draw_scoreboard(self):
        to_write = f"Score: {self.score}"
        self.clear()
        self.write(to_write, align=ALIGN, font=FONT)

    def write_game_over(self):
        self.clear()
        self.goto(0, 40)
        self.write("GAME OVER", align=ALIGN, font=("Courier", 40, "bold"))
        self.goto(0, -40)
        self.write(f"Final Score: {self.score}", align=ALIGN, font=("Courier", 30, "bold"))
