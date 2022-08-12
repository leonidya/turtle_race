import turtle
from turtle import Turtle, Screen
import random
all_turtles = []
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: "
                                                          "red, orange, yellow, blue or purple")
colors = ["red", "orange", "yellow", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50]

for turtle_index in range (0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            if turtle.pencolor() == user_bet:
                print("You Win")
            else:
                print(f"You Lose, the winn is {turtle.pencolor()}")
            is_race_on = False

screen.exitonclick()
