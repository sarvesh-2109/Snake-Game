from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.color("white")
        self.goto(0, 0)
        self.write(f"GAME OVER", font=FONT, align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
