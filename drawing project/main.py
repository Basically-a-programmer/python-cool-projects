import random
import turtle

import color_pic
import random
from turtle import Turtle , Screen
turtle.colormode(255)


my_turtle = Turtle()
my_turtle.screen.bgcolor("black")
x_cor = my_turtle.xcor()
y_cor = my_turtle.ycor()
y_cor -=200
my_turtle.penup()
my_turtle.sety(y_cor)
my_turtle.pendown()
for val2 in range(0,10):
    for val1 in range(0,10):
        my_turtle.dot(20,color_pic.rgb_colours[random.randint(0,33)])
        my_turtle.penup()
        my_turtle.forward(50)
        my_turtle.pendown()

    my_turtle.penup()
    my_turtle.setx(x_cor)
    y_cor += 50
    my_turtle.sety(y_cor)
    my_turtle.pendown()











screen = Screen()

screen.exitonclick()
