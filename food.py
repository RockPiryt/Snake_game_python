from turtle import Turtle
import random


class Food(Turtle):#superclass

    def __init__(self):
        super().__init__()
        self.shape("circle")#method of turtle
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # streching turtle
        self.color("red")
        self.speed("fastest")#I don't see the animation from point 0,0 to random point
        self.refresh()

    def refresh(self):#Important self in parenthesis
        random_x = random.randint(-240, 240)
        random_y = random.randint(-240, 240)
        self.goto(random_x,random_y)
        