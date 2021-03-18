# This class is all about ball which is used in pong game

# Importing module
from turtle import Turtle

# Creating ball class and inheriting Turtle class from turtle module To get all its functionality
class Ball(Turtle):
    def __init__(self):
        # calling Turtle class init method ( constructor )
        super().__init__()
        # Calling create ball method so that whenever we run it wall 1st create ball
        self.create_ball()
        # positions and speed
        self.x = 10
        self.y = 10
        self.ball_speed = 0.1
        
# Create ball function
    def create_ball(self):
        # shape of turtle (ball)
        self.shape("circle")
        self.color("white")
        
        # So that it will not draw line
        self.penup()
        
# For movement of ball it will change its position 
    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        # it will automatically call turtle class method to move ball at new position
        self.goto(new_x, new_y)

# For bouncing y axis
    def bounce_y(self):
        self.y *= -1
        self.ball_speed *= 0.9
        
 # for x axis
    def bounce_x(self):
        self.x *= -1

 # Whenever ball collaps this function will get call at its original position
    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()

