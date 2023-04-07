from turtle import Turtle

#CONSTANS
START_POSITION = [(0, 0), (-20, 0), (-40,0)]# constans capitalize letter
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = [] #list for segments
        self.create_snake() # method for creating snake when we made instance of Snake
        self.head = self.segments[0]#first segment = snake head, it should be under create_snake()

    def create_snake(self):#self in parenthesis
        for position_s in START_POSITION:
            self.add_segment(position_s)
    
    def add_segment(self, position_s):
        new_segment = Turtle(shape='square')
        new_segment.color('lime')
        new_segment.penup()
        new_segment.goto(position_s)
        self.segments.append(new_segment)#self important !!!

    def extend(self):
        #Add new segment to end of snake
        self.add_segment(self.segments[-1].position())
        # position is Turtle_class.method-current location
        # segments[-1] - last segment from list segments
        
    
    def reset_snake(self):
        #remove created snake form screen
        for seg in self.segments:
            seg.goto(1000,1000)
        #create new_snake - repeat what we do in init section
        self.segments.clear() # clear list with all segments
        self.create_snake() # create new snake
        self.head = self.segments[0]# set head of new_snake

    def move(self):
        for seg_num in range (len(self.segments) -1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    #Control snake methods
    def up(self):
        # avoid strange moves, player can't move up when press Down_key
        if self.head.heading() != DOWN: # heading show current head position/directions
            self.head.setheading(UP) # snake head - (first segment) self.segments[0] !!!

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
