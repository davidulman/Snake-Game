from turtle import Turtle


STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.cubes = []
        self.create_snake()
        self.head = self.cubes[0]

    def create_snake(self):
        for pos in STARTING_POS:
            new_cube = Turtle("square")
            new_cube.color("white")
            new_cube.penup()
            new_cube.goto(pos)
            self.cubes.append(new_cube)

    def move(self):
        for cube in range(len(self.cubes) - 1, 0, -1):
            new_x = self.cubes[cube - 1].xcor()
            new_y = self.cubes[cube - 1].ycor()
            self.cubes[cube].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_new_cube(self, pos):
        new_cube = Turtle("square")
        new_cube.color("white")
        new_cube.penup()
        new_cube.goto(pos)
        self.cubes.append(new_cube)

    def extend(self):
        self.add_new_cube(self.cubes[-1].position())
