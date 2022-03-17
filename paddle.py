from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pad_color, pos):
        super().__init__()
        self.shape("square")
        self.color(pad_color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

