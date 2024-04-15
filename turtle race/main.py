from turtle import Turtle , Screen

import random

screen  = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")

user_pick = screen.textinput(title="User pick",prompt="Enter your turtle from rainbow color")
import temp
temp.making_track()
import race
race.start_point()
race.run()
win = race.winner()

if win.lower() == user_pick.lower():
    print("Your turtle won the game")
else:
    print(f"{user_pick} turtle lost , the winner is {win}")

screen.bye()

screen.exitonclick()



