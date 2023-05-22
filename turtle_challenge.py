from turtle import Turtle, Screen
from random import randint, choice

screen = Screen()
screen.colormode(255)

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

# Drawing a square

# for _ in range(4):
#     timmy.fd(25)
#     timmy.right(90)

# Drawing a dashed line

# for _ in range(50):
#     timmy.fd(10)
#     timmy.penup()
#     timmy.fd(10)
#     timmy.pendown()

# Drawing triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon .. one side common

# color_range = (0, 255)
# for i in range(3, 11):
#     r = randint(*color_range)
#     g = randint(*color_range)
#     b = randint(*color_range)
#     timmy.pencolor(r,g,b)
#     for n in range(i):        
#         timmy.fd(100)
#         timmy.right(360 / i)

# Random Walk

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# timmy.pensize(10)
# angles = [0, 90, 180, 270]
    
# while True:
#     timmy.pencolor(choice(colors))
#     timmy.fd(30)
#     timmy.setheading(choice(angles))

# Spirograph
timmy.speed("fastest")
for i in range(0,360,3):
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    timmy.pencolor(color)
    timmy.setheading(i)
    timmy.circle(100)


screen.exitonclick()



