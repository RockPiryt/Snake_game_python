from turtle import Turtle

#Constans for Score
ALLIGMENT = "center"
FONT = ("Arial", 14, "normal")

#Constans for Game Over
ALLIGMENT_G = "center"
FONT_G = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()#Hide arrow
        self.penup()
        self.show_score()

    def show_score(self): #To avoid double text
        self.goto(240, -280)
        self.color('white') # Color before show_text!!!
        self.write(f"Score: {self.score}", move=False, align=ALLIGMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color('white') # Color before show_text!!!
        self.write(f"GAME OVER", move=False, align=ALLIGMENT_G, font=FONT_G)
    

    def update(self):
        self.score += 1
        self.clear()#To clear previous score!!!
        self.show_score()
    