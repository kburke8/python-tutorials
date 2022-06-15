from turtle import Screen, Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        for position in [(0, 0), (-20, 0), (-40, 0)]:
            self.initialize_snake_segment(position)
        self.head = self.segments[0]
        self.grow = False

    def initialize_snake_segment(self, seg_position):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(seg_position)
        self.segments.append(segment)

    def move(self):
        if self.grow:
            new_segment_position = self.segments[-1].position()

        for seg_num in range(len(self.segments) - 1, -1, -1):
            if seg_num == 0:
                self.head.forward(20)
            else:
                self.segments[seg_num].goto(self.segments[seg_num - 1].position())
                self.segments[seg_num].setheading(self.segments[seg_num - 1].heading())
        if self.grow:
            self.initialize_snake_segment(new_segment_position)
            self.grow = False

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

