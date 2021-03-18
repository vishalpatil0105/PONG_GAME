from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
import random

is_on = True
screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle = Paddle(350, 0)
paddle_2 = Paddle(-350, 0)

score = Scoreboard()

screen.listen()
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")
screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")

pong = Ball()

while is_on:
    time.sleep(pong.ball_speed)
    screen.update()
    pong.move()
    # Detect collision with upper wall and down wall
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce_y()

    # Detect collision with left paddle
    if pong.distance(paddle) < 50 and pong.xcor() > 320:
        pong.bounce_x()


    # Detect Collision with right paddle

    if pong.distance(paddle_2) < 50 and pong.xcor() < -320:
        pong.bounce_x()

    # Detect if ball passes right side
    if pong.xcor() > 380:
        pong.reset_position()
        score.left_score_update()

    # Detect if ball passes left side
    if pong.xcor() < -380:
        pong.reset_position()
        score.right_score_update()


screen.exitonclick()