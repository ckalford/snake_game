from turtle import Turtle
import random

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
colors = ["green", "white", "blue", "yellow", "red"]

class Snake:
    def __init__(self):
        self.snake_objects = []
        self.create_snake()
        self.head = self.snake_objects[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        new_snake_object = Turtle("square")
        new_snake_object.color(random.choice(colors))
        new_snake_object.pu()
        new_snake_object.goto(position)
        self.snake_objects.append(new_snake_object)

    def extend(self):
        self.add_segment(self.snake_objects[-1].position())

    def move(self):
        for snake in range((len(self.snake_objects) - 1), 0, -1):
            new_x = self.snake_objects[snake - 1].xcor()
            new_y = self.snake_objects[snake - 1].ycor()
            self.snake_objects[snake].goto(new_x, new_y)
        self.snake_objects[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.snake_objects[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.snake_objects[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.snake_objects[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.snake_objects[0].setheading(RIGHT)




