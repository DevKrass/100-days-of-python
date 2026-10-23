from turtle import Turtle

TEXT_POSITION = (0, 260)
ALIGNEMNT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(TEXT_POSITION)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNEMNT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNEMNT, font=FONT)
