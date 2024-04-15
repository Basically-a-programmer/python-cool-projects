from turtle import Turtle, Screen


def making_track():
    start = Turtle()
    end = Turtle()
    start.goto(-350, -300)
    end.goto(350, -300)
    start.left(90)
    end.left(90)
    start.shape("turtle")
    end.shape("turtle")
    start.pencolor("green")
    end.pencolor("red")
    start.pensize(5)
    end.pensize(5)
    start.forward(600)
    end.forward(600)





