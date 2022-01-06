from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make your bet ", 
        prompt="Choose racer for bet. \nRed | Orange | Yellow | Green | Blue | Purple ").lower()
is_game_on = False


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
l_min = -125
all_turtles = []
for i in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.speed(0)
    new_turtle.goto(x=-230, y=l_min)
    all_turtles.append(new_turtle)
    l_min += 50


if user_bet: # Run's if user_bet is not None.
    is_game_on = True


while is_game_on:
    for turtle in all_turtles:
        new_distance = randint(0, 10)
        turtle.forward(new_distance)
        if turtle.xcor() >= 230:
            if turtle.pencolor() == user_bet:
                print(f"You've won. Winner {turtle.pencolor()} turtle.")
            else:
                print(f"You've lost. Winner {turtle.pencolor()} turtle.")
            is_game_on = False
            


screen.exitonclick()
