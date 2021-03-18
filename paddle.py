# This Class is all for paddle for both right and left we can create it by creating two objects

# Modules
from turtle import Turtle

# Creating Paddle class form inheriting Turtle class
class Paddle(Turtle):
    # For position of paddle
    def __init__(self, x, y):
        x_pos = x
        y_pos = y
        super().__init__()
        self.create_paddle(x_pos, y_pos)

# Create paddle taking position (right/left paddle)
    def create_paddle(self, x, y):
        self.shape("square")
        self.color("white")
        
        # To increase turtle size ( paddle)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

  # For positioning of paddle when user press up down or w and s button
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
