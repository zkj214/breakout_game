from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,10)
        self.color("lime")
        self.penup()
        self.goto(0, -250)

    def move_left(self):
        self.backward(50)

    def move_right(self):
        self.forward(50)




