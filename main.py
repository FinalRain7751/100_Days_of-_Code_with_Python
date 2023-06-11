from turtle import Turtle, Screen, done
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

INITIAL_SLEEP_TIME = 0.39

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
sleep_for = INITIAL_SLEEP_TIME
snake = Snake()    
food = Food()
score = Scoreboard()
screen.update()

def listen_for_keypress(snake):
    screen.listen()
    screen.onkeypress(snake.turn_south, key="Down")
    screen.onkeypress(snake.turn_north, key="Up")
    screen.onkeypress(snake.turn_east, key="Right")
    screen.onkeypress(snake.turn_west, key="Left")

def check_game_status(snake):
    head_xcor = snake.head.xcor()
    head_ycor = snake.head.ycor()

    if head_xcor > 280 or head_xcor < -280:
        reset_game() 
    
    if head_ycor >= 280 or head_ycor <= -280:
        reset_game() 
        
    for i in range(len(snake.body)):
        if snake.head.distance(snake.body[i]) < 10:        
            reset_game()

def reset_game():
    global snake
    global sleep_for
    for i in range(len(snake.snakes)):
        snake.snakes[i].hideturtle()
        snake.snakes[i].reset()

    snake = Snake()
    listen_for_keypress(snake)
    sleep_for = INITIAL_SLEEP_TIME
    score.update_highscore()

listen_for_keypress(snake)
while True:
    check_game_status(snake)
    screen.update()
    snake.move_snake()
    time.sleep(sleep_for)
    if snake.head.distance(food) < 15:
        snake.create_new_segment()
        food.move_food()        
        score.update_score()
        if sleep_for > 0.1:
            sleep_for -= 0.1

    
screen.exitonclick()
