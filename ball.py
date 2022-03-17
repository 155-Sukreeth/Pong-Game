from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_x_by = 10
        self.move_y_by = 10

    def move(self):
        new_x = self.xcor() + self.move_x_by
        new_y = self.ycor() + self.move_y_by
        self.goto(x=new_x, y=new_y)

    def bounce_Wall(self):
        self.move_y_by *= -1

    def bounce_Pad(self):
        self.move_x_by *= -1

    def refresh(self):
        self.goto(0, 0)
