import turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.heads = []
        self.create_snake()
        self.head = self.heads[0]

    def create_snake(self):
        for i in START_POS:
            self.add_head(i)

    def add_head(self, position):
        new_segment = turtle.Turtle()
        new_segment.penup()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.shapesize(1, 1)
        new_segment.goto(position)
        self.heads.append(new_segment)

    def move(self):
        for seg_num in range(len(self.heads) - 1, 0, -1):
            x = self.heads[seg_num - 1].xcor()
            y = self.heads[seg_num - 1].ycor()
            self.heads[seg_num].goto(x, y)
        self.heads[0].forward(MOVE_DISTANCE)

    def extends(self):
        self.add_head(self.heads[-1].position())

    def up(self):
        if self.heads[0].heading() != DOWN:
            self.heads[0].setheading(UP)

    def down(self):
        if self.heads[0].heading() != UP:
            self.heads[0].setheading(DOWN)

    def left(self):
        if self.heads[0].heading() != RIGHT:
            self.heads[0].setheading(LEFT)

    def right(self):
        if self.heads[0].heading() != LEFT:
            self.heads[0].setheading(RIGHT)

    def reset(self):
        for i in self.heads:
            i.goto(1000, 1000)
        self.heads.clear()
        self.create_snake()
        self.head = self.heads[0]