from turtle import Turtle, Screen
import random

def start_point():
    red.shape("turtle")
    green.shape("turtle")
    blue.shape("turtle")
    orange.shape("turtle")
    violet.shape("turtle")
    yellow.shape("turtle")
    indigo.shape("turtle")

    red.color("red")
    green.color("green")
    blue.color("blue")
    orange.color("orange")
    violet.color("violet")
    yellow.color("yellow")
    indigo.color("indigo")

    red.penup()
    green.penup()
    blue.penup()
    orange.penup()
    violet.penup()
    yellow.penup()
    indigo.penup()

    red.goto(-350, -250)
    green.goto(-350, -200)
    blue.goto(-350, -150)
    orange.goto(-350, -100)
    violet.goto(-350, 0)
    yellow.goto(-350, 50)
    indigo.goto(-350, 100)


def run():
    red.forward(random.randint(0,10))
    green.forward(random.randint(0,10))
    blue.forward(random.randint(0,10))
    orange.forward(random.randint(0,10))
    violet.forward(random.randint(0,10))
    yellow.forward(random.randint(0,10))
    indigo.forward(random.randint(0,10))

def winner():
    if red.xcor() >= 249:
        win = "red"
        return win
    elif yellow.xcor() >= 249:
        win = "yellow"
        return win
    elif green.xcor() >= 249:
        win = "green"
        return win
    elif blue.xcor() >= 249:
        win = "blue"
        return win
    elif violet.xcor() >= 249:
        win = "violet"
        return win
    elif orange.xcor() >= 249:
        win = "orange"
        return win
    else:
        win = "indigo"
        return win

red = Turtle()
orange = Turtle()
blue = Turtle()
green = Turtle()
violet = Turtle()
yellow = Turtle()
indigo = Turtle()


start_point()
while red.xcor()<350 and orange.xcor()<350 and yellow.xcor()<350 and green.xcor()<350 and blue.xcor()<350 and violet.xcor()<350 and indigo.xcor()<350:
    run()



