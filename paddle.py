from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.setheading(90)
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5)
        self.goto(x_cor, y_cor)

    def up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
