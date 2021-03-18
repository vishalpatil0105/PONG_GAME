# This Class will track all score for each side 

# Module
from  turtle import Turtle

# creatinf Scoreboard class inheritaed from Turtle class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        
        # Initial Scores
        self.left_score = 0
        self.right_score = 0
        self.update_score()

# To update score whenever each one hits the edge of miss ball
    def update_score(self):
        # Clearing score to put new score
        self.clear()
        # Position
        self.goto(-100, 200)
        # Giving position and required data to write on Turtle
        self.write(self.right_score, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.left_score, align="center", font=("courier", 80, "normal"))
      
# For updating left score 

    def left_score_update(self):
        self.left_score += 1
        self.update_score()
        
 # For updating right score
    def right_score_update(self):
        self.right_score += 1
        self.update_score()
