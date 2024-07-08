import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.respawn()

    def respawn(self):
        r_x = random.randint(-280, 280)
        r_y = random.randint(-280, 280)
        self.goto(r_x, r_y)
