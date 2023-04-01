from turtle import Turtle

ALLIGMENT = 'center'
FONT = ('Courier', 30, 'bold')

class Title(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,255)
        self.color('lime')
        self.write('SNAKE GAME', align=ALLIGMENT, font=FONT)
