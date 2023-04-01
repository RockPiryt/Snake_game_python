#snake game


from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


#Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black') #kolor tła
screen.title('Snake game in Python')
screen.tracer(0)#wyłaczy zeby zdecydowac kiedy odswiezac ekran

snake = Snake()


#Snake lists
start_position = [(0, 0), (-20, 0), (-40,0)]#tuple for both coordinates
snake_segments = []

#Create snake body
for position in start_position:
    snake_seg = Turtle(shape='square')
    snake_seg.color('white')
    snake_seg.penup()
    snake_seg.goto(position)
    snake_segments.append(snake_seg)

# screen.update()#odswiezenie ekranu



#Automating snake moves forward
game_is_on = True
while game_is_on:
    #Animating
    screen.update()#odswiezenie ekranu
    time.sleep(0.1)#określenie czasu co ile odświeza
# #Move snake from last segment
    for seg_num in range (len(snake_segments) -1,0,-1):
        new_x = snake_segments[seg_num-1].xcor()#seg_num-1 to przedostani element[index=1]
        new_y = snake_segments[seg_num-1].ycor()
        snake_segments[seg_num].goto(new_x,new_y)#ostatni segment
    snake_segments[0].forward(20)#ruszenie pierwszym segmentem do przodu



















##########################################################################;;;;;;;;;;;;;;;;;               

#Animating snake segments informations
game_is_on = True
while game_is_on:
    screen.update()#odswiezenie ekranu
    time.sleep(0.1)#określenie czasu co ile odświeza
# #Move snake from last segment
    # for seg_num in range (2,0,-1):
    for seg_num in range (len(snake_segments) -1,0,-1):
        # cała lista -1 żeby uzyskać ostatni index
        # (start=3, stop=1, step=-1): wygneruje ->  3 2 1, step -1 liczy od końca
        #    index            0          1       2
        # start_position = [(0, 0), (-20, 0), (-40,0)]
        #dlatego zmieniamy indexy
        # (start=2, stop=0, step=-1): wygneruje ->  2,1,0 step -1 liczy od końca
        # w range nie działa key word
        new_x = snake_segments[seg_num-1].xcor()#seg_num-1 to przedostani element[index=1]
        new_y = snake_segments[seg_num-1].ycor()
        snake_segments[seg_num].goto(new_x,new_y)#ostatni segment
    snake_segments[0].forward(20)#ruszenie pierwszym segmentem do przodu
    # snake_segments[0].left(90)#ruszenie pierwszym segmentem w lewo

        #odliczaenie seg_num
        # seg_num=2
        # seg_num=1
        # seg_num=0




    #pierwotna wersja bez linkowania obiektów
    # for seg in snake_segments:
    #     seg.forward(20)#pójdzie do przodu ale nie będzie skręcać dobrze
    #snake_segments[0].left(90)# ta funkcja nie działa - trzeba od końca zacząć ruch



screen.exitonclick()