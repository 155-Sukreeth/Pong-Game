from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

# screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# create paddles
# player 1
player1 = Paddle("red",(350,0))
scoreP1 = Scoreboard((40, 210), "Registrar")

# player 2
player2 = Paddle("green",(-350,0))
scoreP2 = Scoreboard((-40,210), "Students")

# ball
ball = Ball()

# screen commands
screen.listen()
screen.onkey(player1.go_up,"Up")
screen.onkey(player1.go_down,"Down")
screen.onkey(player2.go_up,"w")
screen.onkey(player2.go_down,"s")

# start game
is_GameOn = True
while is_GameOn:
    screen.update()
    ball.move()

    # score
    if ball.xcor()>360:
        scoreP2.increase_score()
        ball.refresh()
        time.sleep(1)
    elif ball.xcor()<-360:
        scoreP1.increase_score()
        ball.refresh()
        time.sleep(1)
    # collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_Wall()
    # collision with paddle
    if ball.xcor()>320 or ball.xcor()<-320:
        if ball.distance(player1)<50 or ball.distance(player2)<50:
            ball.bounce_Pad()

    # GAME OVER
    if scoreP1.score == 5:
        scoreP1.game_ended()
        is_GameOn = False
    elif scoreP2.score == 5:
        scoreP2.game_ended()
        is_GameOn = False

    time.sleep(0.1)

screen.exitonclick()