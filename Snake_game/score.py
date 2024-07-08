from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.u_scoreboard()
        self.hideturtle()

    def u_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1

        self.u_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.u_scoreboard()

