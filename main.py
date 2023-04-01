


####################   SNAKE GAME   ###########################

#Imports
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from title import Title
from field import Field
import time


#Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black') 
screen.title('Snake game in Python')
screen.tracer(0)

#Create title
title = Title()

#Create field
field = Field()

#Create snake
snake = Snake()#trigger a create_snake method 

#Snake control by keys
screen.listen()
screen.onkey(snake.up, "Up")#Capitalize letter for arrows
screen.onkey(snake.down,"Down")#func and key in parenthesis
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

#Create food
food = Food()

#Create scoreboard
scoreboard = Scoreboard()

#Game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    #Snake moving
    snake.move()

    #Detect collision with food = update scoreboard = extend snake
    if snake.head.distance(food) < 15:
        #print('nom nom nom')
        food.refresh()#self method from food class
        snake.extend()
        scoreboard.update()#self method from scoreboard class

    #End game 
    #Detect collision with wall - 
    #In while loop to stop the loop!!
    FIELD_SIZE = 257
    if snake.head.xcor() > FIELD_SIZE or snake.head.xcor() < -FIELD_SIZE or snake.head.ycor() > FIELD_SIZE or snake.head.ycor() < -FIELD_SIZE:
        game_is_on = False#Stop loop condition
        scoreboard.game_over()#Use method from scoreboard class to end game
        # print('GAME OVER')


    #Collision with tail
    #if head collides with tail any segment in the tail:
        #trigger game_over
    for segment in snake.segments:#loop for every segments
        #to avoid  touching head case
        if segment == snake.head:#without this game is end
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

#Exit game
screen.exitonclick()