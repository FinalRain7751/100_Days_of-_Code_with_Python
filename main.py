from screen import game_screen, HEIGHT, WIDTH
from score import Scoreboard
from ball import Ball
from paddle import Paddle
import time

screen = game_screen()
scoreboard = Scoreboard()
ball = Ball()
paddle = Paddle()
screen.update()

def has_player_won():
    if ball.xcor() > WIDTH/2 - 25:
        return True
    return False

def has_cpu_won():
    if ball.xcor() < WIDTH/2 - 20:
        return True
    return False

screen.listen()
screen.onkeypress(paddle.move_player_paddle_up, key="w")
screen.onkeypress(paddle.move_player_paddle_down, key="s")
screen.onkeypress(paddle.move_cpu_paddle_up, key="Up")
screen.onkeypress(paddle.move_cpu_paddle_down, key="Down")


while ball.ycor() > -(HEIGHT/2 - 10):
   ball.ball_starts_moving()
   time.sleep(0.01)
   screen.update()

ball.ball_set_initial_direction()

while has_player_won() == False and has_cpu_won() == False:    
    ball.ball_moving()
    time.sleep(0.01)
    screen.update()






screen.exitonclick()