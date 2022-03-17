from turtle import Turtle

# constants
ALIGNMENT = "center"
FONT = ("courier", 50, "normal")

class Scoreboard(Turtle):
    def __init__(self, pos, name):
        super().__init__()
        self.score = 0
        self.name = name
        self.penup()
        self.color("white")
        self.goto(pos)
        self.write(arg=f"{self.score}", align=ALIGNMENT, font= FONT)
        self.hideturtle()

    def increase_score(self):
        self.score +=1
        self.clear()
        self.write(arg=f"{self.score}", align=ALIGNMENT, font=FONT)

    def game_ended(self):
        self.penup()
        self.color("white")
        self.goto(x=0, y=0)
        self.write(arg=f"GAME OVER!!{self.name} WINS!", align=ALIGNMENT, font=("courier", 20, "normal"))
        self.hideturtle()
