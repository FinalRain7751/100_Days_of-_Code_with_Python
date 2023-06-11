from turtle import Turtle
from random import randrange, choice
from screen import WIDTH, HEIGHT

COLORS = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
CAR_LENGTH = 2
START_SPEED = 5
SPEED_INCREMENT = 2.5

class Traffic():
    def __init__(self):
        self.traffic = []
        self.speed = START_SPEED
        
    def generate_traffic(self):
        chance = randrange(1,7)
        if chance == 1:
            originY = randrange(-HEIGHT/2 + 60, HEIGHT/2 - 60, 5)
            originX = WIDTH/2 + 10                 
            origin = (originX, originY)
            car = self.create_car(origin)
            self.traffic.append(car)

    def move_traffic(self):
        for car in self.traffic:
            car.fd(self.speed)

    def increase_speed(self):
        self.speed += SPEED_INCREMENT

    def create_car(self, origin):
        
        color = choice(COLORS)
        car = Turtle()
        self.car_setup(car, color)
        car.goto(origin)
        return car
        
        
    def car_setup(self, car, color):
        car.resizemode('user')
        car.shape('square')
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.setheading(180)
        car.color(color)
        car.penup()

    def clear_traffic(self):
        for car in self.traffic:
            car.hideturtle()

    def remove_passed_cars(self):
        for i, car in enumerate(self.traffic):
            if car.xcor() < -WIDTH/2 - 40:
                car.reset()
                car.hideturtle()
                self.traffic.pop(i)

