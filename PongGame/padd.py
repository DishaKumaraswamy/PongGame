from turtle import Turtle

class Paddle(Turtle) :
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        y_val = self.ycor() + 30
        self.goto(self.xcor(), y_val)

    def down(self):
        y_val = self.ycor() - 30
        self.goto(self.xcor(), y_val)