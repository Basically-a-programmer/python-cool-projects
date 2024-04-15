import turtle
from turtle import Screen
import time
import snake
import food
import score


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
start_pos = [(0,0),(-20,0),(-40,0)]

diff = turtle.textinput("Difficulty","Pick your difficulty level EASY/MEDIUM/HARD")
if diff.lower() =="easy":
    snake.move_dis = 10
elif diff.lower() == "medium":
    snake.move_dis = 15
else:
    snake.move_dis = 20

snake = snake.Snake()
foods = food.Food()
score_board = score.Score_board()
screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.lefts,"a")
screen.onkey(snake.rights,"d")


screen.update()
game_on = True

while game_on:
    screen.update()
    time.sleep(0.05)
    snake.move()
#     collision with foodd
    if snake.head.distance(foods) < 15:
        foods.refresh()
        score_board.update()
        snake.extend()

    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        score_board.reset_score()
        snake.reset_game()

    for segments in snake.segments[1:len(snake.segments)]:
        if snake.head.distance(segments) < 10:
            score_board.reset_score()


            snake.reset_game()

screen.exitonclick()