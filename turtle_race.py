from turtle import Turtle, Screen, resetscreen
from random import randint

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]


def main():
    screen = Screen()
    screen.setup(height=600, width=800)

    player_turtle = screen.textinput(
        "Choose a turtle from: violet, indigo, blue, green, yellow, orange, red.",
        "Enter the color of the turtle you want to play with.",
    )

    turtles = []

    for color in colors:
        timmy = Turtle()
        timmy.shape("turtle")
        timmy.color(color)
        timmy.penup()
        starting_y = 150 - (colors.index(color) * 50)
        timmy.goto(-390, starting_y)
        turtles.append(timmy)

    winning_turtle = race(turtles)
    if winning_turtle == player_turtle:
        print("You won.")
    else:
        print(f"You lost. The {winning_turtle} turtle won the race.")

    screen.exitonclick()


def race(turtles):
    while True:
        for turtle in turtles:
            if is_winner(turtle):
                winner = turtle.pencolor()
                resetscreen()
                return winner
            move_turtle(turtle)


def move_turtle(timmy):
    current_x = timmy.xcor()
    move = randint(1, 20)
    if (current_x + move) > 390:
        move = 390 - current_x
    timmy.fd(move)


def is_winner(timmy):
    if timmy.xcor() == 390:
        return True
    return False


if __name__ == "__main__":
    main()
