from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos, shape="square"):
        super().__init__(shape)
        self.goto(350, 0)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)
        self.color("white")

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
