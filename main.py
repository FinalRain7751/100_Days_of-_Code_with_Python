from screen import game_screen
from score import Scoreboard
from ball import Ball
from paddle import Paddle
import time

screen = game_screen()
scoreboard = Scoreboard()
ball = Ball()
paddle = Paddle()
screen.update()

def is_game_on():
    
    return True

screen.listen()
while is_game_on():
    screen.onkeypress(paddle.move_player_paddle_up, key="w")
    screen.onkeypress(paddle.move_player_paddle_down, key="s")
    screen.onkeypress(paddle.move_cpu_paddle_up, key="Up")
    screen.onkeypress(paddle.move_cpu_paddle_down, key="Down")
    time.sleep(0.01)
    screen.update()


# screen.onkey(ball.start_moving, key="Space")




screen.exitonclick()