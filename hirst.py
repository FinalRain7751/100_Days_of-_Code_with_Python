import colorgram
from turtle import Turtle, Screen 
from random import choice

timmy = Turtle()

screen = Screen()
screen.bgcolor("lightgray")
screen.colormode(255)

timmy.shape("turtle")
timmy.color("blue")

colors = colorgram.extract("image.jpg", 100)

def draw_hirst(timmy):
    timmy.ht()
    timmy.penup()
    timmy.setposition(-200, -200)
    timmy.pendown()
    for i in range(10):
        for _ in range(10):
            color = choice(colors).rgb
            timmy.color(color.r, color.g, color.b)
            timmy.begin_fill()
            timmy.dot(15)
            timmy.end_fill()
            timmy.penup()
            timmy.fd(40)
            timmy.pendown()
        timmy.penup()
        x = timmy.xcor()
        y = timmy.ycor()
        timmy.setposition(x-400, y+40)
        timmy.pendown()

draw_hirst(timmy)

screen.exitonclick()