from turtle import Turtle
import random

colors = ['light blue', 'royal blue',
              'light steel blue', 'steel blue',
              'light cyan', 'light sky blue',
              'violet', 'salmon', 'tomato',
              'sandy brown', 'purple', 'deep pink',
              'aqua', 'khaki']

weights = [1, 2, 1, 1, 3, 2, 1, 4, 1, 3,
           1, 1, 1, 4, 1, 3, 2, 2, 1, 2,
           1, 2, 1, 2, 1]

class Brick(Turtle):
    def __init__(self,x_cor,y_cor):
        super().__init__()
        self.shape("square")
        self.shapesize(1.5,3)
        self.color(random.choice(colors))
        self.penup()
        self.quality = random.choice(weights)
        self.goto(x_cor, y_cor)
class Bricks:
    def __init__(self):
        self.y_start = 0
        self.y_end = 240
        self.all_bricks = []
        self.create_all_lanes()

    def create_all_lanes(self):
        for y in range(self.y_start, self.y_end, 32):
            for x in range(-470, 470, 62):
                brick = Brick(x,y)
                self.all_bricks.append(brick)

