from turtle import Turtle

start_pos = [(0,0),(-20,0),(-40,0)]
move_dis = 10
class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for val in start_pos:
            new_tur = Turtle("square")
            new_tur.color("white")
            new_tur.penup()
            new_tur.goto(val)
            self.segments.append(new_tur)
            self.head = self.segments[0]

    def move(self):
        for segn_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[segn_num - 1].xcor()
            new_y = self.segments[segn_num - 1].ycor()
            self.segments[segn_num].goto(new_x, new_y)
        self.segments[0].forward(move_dis)

    def reset_game(self):
        self.write(f"Game over", align="center", font=("Courier", 15, "normal"))
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    def add_segment(self,position):
        new_tur = Turtle("square")
        new_tur.color("white")
        new_tur.penup()
        new_tur.goto(position)
        self.segments.append(new_tur)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def up(self):
        self.segments[0].setheading(90)

    def lefts(self):
        self.segments[0].setheading(180)
    def rights(self):
        self.segments[0].setheading(0)
    def down(self):
        self.segments[0].setheading(270)