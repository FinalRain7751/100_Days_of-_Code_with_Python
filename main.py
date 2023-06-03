from screen import game_screen, number_of_players, HEIGHT, WIDTH
from score import Scoreboard
from ball import Ball, INITIAL_SPEED
from paddle import Paddle
import time




screen = game_screen()
number_of_players = number_of_players(screen)

scoreboard = Scoreboard(number_of_players)
ball = Ball()
paddle = Paddle(number_of_players)
screen.update()
start = "player"


def is_game_on():
    return True

def has_player1_won():
    global start
    if ball.xcor() > WIDTH/2 - 25 -10:
        scoreboard.player1_score +=1
        scoreboard.update_score()
        ball.home()
        start = "player1"        
        return True
    return False

def has_player2_won():
    global start
    if ball.xcor() < -(WIDTH/2 - 20 - 10):
        scoreboard.player2_score +=1
        scoreboard.update_score()
        ball.home()
        start = "player2"
        return True
    return False

def has_cpu_won():
    global start
    if ball.xcor() < -(WIDTH/2 - 20 - 10):
        scoreboard.cpu_score +=1
        scoreboard.update_score()
        ball.home()
        start = "cpu"
        return True
    return False

def is_winner():
    if number_of_players == 1:
        if has_player1_won() or has_cpu_won():
            return True
    elif number_of_players == 2:
        if has_player1_won() or has_player2_won():
            return True
    return False

screen.listen()
screen.onkeypress(paddle.move_player1_paddle_up, key="w")
screen.onkeypress(paddle.move_player1_paddle_down, key="s")
screen.onkeypress(paddle.move_player2_paddle_up, key="Up")
screen.onkeypress(paddle.move_player2_paddle_down, key="Down")

while is_game_on():
    ball.starts_moving(start)
    while True:
        if is_winner():
            ball.speed = INITIAL_SPEED
            paddle.reset_position()
            break 
        else:  
            if ball.is_hitting_paddle(paddle.player1_paddles): 
                if ball.speed < 15:
                    ball.speed += 1
                    print(ball.speed)

            if number_of_players == 2:
                ball.is_hitting_paddle(paddle.player2_paddles)
            else:
                ball.is_hitting_paddle(paddle.cpu_paddles)
                
            ball.is_hitting_wall()    
            ball.moving()
            if number_of_players == 1:
                paddle.move_cpu_paddle(ball)
            time.sleep(0.01)    
            screen.update()

screen.exitonclick()