# This .py file from which we handle all game


# importing all classes (modules)
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
import random

# Varible To continue until we hit wall
is_on = True

# screen class for showing all game
screen = Screen()

# Propertices for screen class object
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

# creating 2 paddles left and right by giving x and y position
paddle = Paddle(350, 0)
paddle_2 = Paddle(-350, 0)

# creating score board object
score = Scoreboard()

# this method is used for listing our key pressing 
screen.listen()

# For right side paddle movement
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")

# for left side paddle movement
screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")

# creating ball using Ball class object
pong = Ball()

# Loop
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

# TO hold our scrren until we click button
screen.exitonclick()
