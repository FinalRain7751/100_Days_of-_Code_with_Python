from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 14, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
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

    def update_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.score = 0
        self.draw_scoreboard()



    def draw_scoreboard(self):
        curr_score = f"Score: {self.score}  "
        high_score = f"  Highscore: {self.highscore}"
        self.clear()
        self.write(curr_score, align='right', font=FONT)
        self.write(high_score, align='left', font=FONT)

    def write_game_over(self):
        self.clear()
        self.goto(0, 40)
        self.write("GAME OVER", align=ALIGN, font=("Courier", 40, "bold"))
        self.goto(0, -40)
        self.write(f"Final Score: {self.score}", align=ALIGN, font=("Courier", 30, "bold"))
