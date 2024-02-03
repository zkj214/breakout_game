from turtle import Turtle
import random

COLOR_LIST = ['light blue', 'royal blue',
              'light steel blue', 'steel blue',
              'light cyan', 'light sky blue',
              'violet', 'salmon', 'tomato',
              'sandy brown', 'purple', 'deep pink',
              'medium sea green', 'khaki','aqua']

FONT = ("Courier", 62, "bold")
FONT2 = ("Courier", 32, "normal")

class UI(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.header()

    def header(self):
        self.color(random.choice(COLOR_LIST))
        self.goto(0,0)
        self.write("B R E A K O U T",align="center",font=FONT)
        self.color("white")
        self.goto(0, -180)
        self.write('Press Space Key to PAUSE the Game',
                   align="center", font=('Calibri', 14, 'normal'))

    def declare_win(self):
        self.color("cyan")
        self.goto(0, -125)
        self.write("YOU WIN!", align="center", font=FONT2)

    def game_over(self):
        self.color("red")
        self.goto(0, -125)
        self.write("GAME OVER", align="center", font=FONT2)



