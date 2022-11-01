import random
import turtle
from turtle import Turtle , Screen

is_race_on = False
screen = Screen()

screen.setup(width = 500 , height=400)
user_bet = screen.textinput(title="Make Your Bet" , prompt= "Which Turtle will win the race ? Enter a color : ")
colors = ["red" , "orange" , "yellow" , "green" , "blue" ,"purple"]
y_positions = [-70 , -40 , -10 , 20 , 50 , 80]
all_turtles = []

for turtle_index in range(0, 6):
    om = Turtle(shape = "turtle")
    om.penup()
    om.color(colors[turtle_index])
    om.goto(x = -230 , y =y_positions[turtle_index])
    all_turtles.append(om)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230 :
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won ! The {winning_color} turtle is the winner ! ")
            else :
                print(f"You lose ! The {winning_color} turtle is the winner ! ")
        random_distance = random.randint(0 , 10)
        turtle.forward(random_distance)


screen.exitonclick()


