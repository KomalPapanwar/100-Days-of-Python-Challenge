from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")

for i in range(0,4):
    timmy.forward(100)
    timmy.left(90)

screen = Screen()
screen.exitonclick()