from turtle import Turtle
ALIGN = "center"
FONT = ("Courier",15,"normal")

# class game_end(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.color("white")
#         self.write(f"Game Over",align=ALIGN,font=FONT)

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.high_score = self.takehigh_score()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score:}",align=ALIGN,font=FONT)
        self.reset_score()
        self.hideturtle()
        self.update_score()

    def takehigh_score(self):
        with open("data.txt") as file:
            content = file.read()
        return content
    def change_score(self):
        with open("data.txt",mode="w") as file:

            file.write(str(self.score))
    def reset_score(self):
        if self.score > int(self.takehigh_score()):
            self.high_score = self.score
            self.change_score()
        self.score = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score:}    High Score : {self.high_score}", align="center", font=("Courier", 15, "normal"))

    def update(self):
        self.score +=1
        # self.write(f"Score: {self.score:}", align="center", font=("Arial", 15, "normal"))

        self.update_score()





