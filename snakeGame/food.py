from turtle import Turtle
import random

ran_x = [260, 240, 220, 200, 180, 160, 140, 120, 100, 0, 20, 40, 60, 80, -20, -40, -60, -80, -100, -120, -140, -160
         , -180, -200, -220, -240, -260]

ran_y = [260, 240, 220, 200, 180, 160, 140, 120, 100, 0, 20, 40, 60, 80, -20, -40, -60, -80, -100, -120, -140, -160
         , -180, -200, -220, -240, -260]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.choice(ran_x)
        random_y = random.choice(ran_y)
        self.goto(random_x, random_y)



