from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-230, 260)
        self.write(f"Level: {self.score}", align=ALIGN, font=FONT)

    def increase_level(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align=ALIGN, font=FONT)
