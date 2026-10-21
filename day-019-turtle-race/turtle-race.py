import random
from turtle import Screen, Turtle

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color"
)

colors = ["red", "orange", "blue", "yellow", "green", "purple"]
all_turtles = []

height = 170
for index in range(6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[index])
    turtle.goto(x=-230, y=height)
    height -= 65
    all_turtles.append(turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won. The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()

# pos = 0
# for _ in range(4):
#     turtle = Turtle()
#     turtle.penup()
#     pos -= 50
#     turtle.setposition(0, pos)
