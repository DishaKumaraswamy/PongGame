from turtle import Screen
from padd import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

sc = Screen()
sc.setup(width=800, height=600)
sc.title("Pong Game")
sc.bgcolor("DarkGoldenrod")
sc.tracer(0)


pd = Paddle((370, 0))
pd1 = Paddle((-380, 0))
ball = Ball()
score = ScoreBoard()

sc.listen()
sc.onkey(pd.up, "Up")
sc.onkey(pd.down, "Down")
sc.onkey(pd1.up, "s")
sc.onkey(pd1.down, "d")


game = True
while game:
    time.sleep(ball.move_speed)
    sc.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()

    if ball.distance(pd) < 50 and ball.xcor() > 350 or ball.distance(pd1) < 50 and ball.xcor() < -360:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_pos()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_pos()
        score.r_point()


sc.exitonclick()