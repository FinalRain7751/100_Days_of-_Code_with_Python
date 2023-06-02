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

def is_game_on():
    return True

def has_player_won():
    if ball.xcor() > WIDTH/2 - 25:
        scoreboard.player_score +=1
        scoreboard.update_score()
        ball.home()
        # if ball.speed <= 6 and scoreboard.ball_increase_speed(scoreboard.player_score):
        #     ball.speed += 1
        print(ball.speed)
        return True
    return False

def has_cpu_won():
    if ball.xcor() < -(WIDTH/2 - 20):
        scoreboard.cpu_score +=1
        scoreboard.update_score()
        ball.home()
        return True
    return False

screen.listen()
screen.onkeypress(paddle.move_player_paddle_up, key="Up")
screen.onkeypress(paddle.move_player_paddle_down, key="Down")
# screen.onkeypress(paddle.move_cpu_paddle_up, key="w")
# screen.onkeypress(paddle.move_cpu_paddle_down, key="s")

while is_game_on():
    ball.starts_moving()
    while True:
        if has_player_won() or has_cpu_won():
            break 
        else:  
            if not ball.is_hitting_paddle(paddle.cpu_paddles): 
                ball.is_hitting_paddle(paddle.player_paddles) 
            ball.is_hitting_wall()    
            ball.moving()
            paddle.move_cpu_paddle(ball)
            time.sleep(0.01)    
            screen.update()

screen.exitonclick()