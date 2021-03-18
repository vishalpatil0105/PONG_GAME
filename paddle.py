from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        x_pos = x
        y_pos = y
        super().__init__()
        self.create_paddle(x_pos, y_pos)

    def create_paddle(self, x, y):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
