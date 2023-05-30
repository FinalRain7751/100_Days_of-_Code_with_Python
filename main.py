from turtle import Turtle, Screen, done
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
sleep_for = 0.39
snake = Snake()    
food = Food()
score = Scoreboard()

screen.listen()
screen.onkeypress(snake.turn_south, key="Down")
screen.onkeypress(snake.turn_north, key="Up")
screen.onkeypress(snake.turn_east, key="Right")
screen.onkeypress(snake.turn_west, key="Left")

def is_game_on(snake):
    head_xcor = snake.head.xcor()
    head_ycor = snake.head.ycor()

    if head_xcor > 280 or head_xcor < -280:
        game_over(snake)
        return False 
    
    if head_ycor >= 280 or head_ycor <= -280:
        game_over(snake)
        return False 
        
    for i in range(len(snake.body)):
        if snake.head.distance(snake.body[i]) < 10:        
            game_over(snake)
            return False
    return True 

def game_over(snake):
    for i in range(len(snake.snakes)):
        snake.snakes[i].reset()
        snake.snakes[i].hideturtle()
    food.hideturtle()
    score.write_game_over()


screen.update()
while is_game_on(snake):
    snake.move_snake()
    time.sleep(sleep_for)
    if snake.head.distance(food) < 15:
        snake.create_new_segment()
        food.move_food()        
        score.update_score()
        if sleep_for > 0.1:
            sleep_for -= 0.1
    screen.update()

    


screen.exitonclick()
screen.mainloop()