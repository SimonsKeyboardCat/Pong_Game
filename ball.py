from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.width = 20
        self.height = 20
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.move_x = 10
        self.move_y = 10

    def move(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.speed_up()
        self.move_x *= -1

    def speed_up(self):
        if self.xcor() > 0:
            self.move_x += 5
        elif self.xcor() < 0:
            self.move_x -= 5

    def reset(self):
        self.goto(0, 0)
        self.move_x = 10
        self.move_y = 10
