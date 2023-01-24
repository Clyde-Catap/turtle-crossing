from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def writee(self, writer):
        self.goto(-220, 260)
        self.write(arg=f"LEVEL: {writer}", move=False, align="center", font=FONT)


    def game_over(self, writer):
        self.goto(0, 0)
        self.write(arg=f"{writer}", move=False, align="center", font=FONT)

