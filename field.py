from turtle import Turtle


class Field(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(255,-255)
        self.color('white')
        self.setheading(45)
        self.circle(357, steps=4)
        self.hideturtle()

