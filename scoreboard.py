from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("yellow")
        self.score=0
        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.display_scoreboard()

    def display_scoreboard(self):
        self.goto(-480, 240)
        self.write(f"{self.score}", align="left", font=("Courier", 35, "bold"))
        self.goto(450, 250)
        self.write(f"High Score: {self.high_score}", align="right", font=("Courier", 20, "normal"))

    def update_scoreboard(self):
        self.score+=4
        self.clear()
        self.display_scoreboard()

    def save_high_score(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",'w') as data:
                data.write(f"{self.high_score}")