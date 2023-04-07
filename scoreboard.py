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
        # self.high_score = 0 #set 0 for start counting - firt way - not saving in txt file 
        with open("data.txt") as data:
            self.high_score = int(data.read())#read 0 from data.txt
        self.hideturtle()#Hide arrow
        self.penup()
        # self.color('white') # Color before show_text!!!
        self.update_score()

    def update_score(self): #To avoid double text
        self.clear()#To clear previous score!!!
        self.goto(-160, -280)
        self.color('white') # Color before show_text!!!
        self.write(f"Score: {self.score}", move=False, align=ALLIGMENT, font=FONT)
        self.goto(160, -280)
        self.color('red') # Color before show_text!!!
        self.write(f"High Score:{self.high_score}", move=False, align=ALLIGMENT, font=FONT)


    def increase_score(self):
        self.score += 1#count
        self.update_score()# show text

    def reset_score(self):
        if self.score > self.high_score:# get the biggest value
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0 # reset to 0 end start new game and counting
        self.update_score()


    # #Game over -stop game
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", move=False, align=ALLIGMENT_G, font=FONT_G)
    

