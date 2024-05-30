from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(0, 280)
        self.score = 0
        self.highscore = self.read_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_score()
        self.score = 0
        self.update_scoreboard()

    def read_score(self):
        with open("data.txt") as file:
            return int(file.read())

    def write_score(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.highscore}")
