from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
  def __init__(self) -> None:
    super().__init__()
    self.score = 0
    self.high_score = 0
    self.hideturtle()
    self.color("white")
    self.penup()
    self.goto(0, 270)
    self.update_scoreboard()
  
  def update_scoreboard(self):
    self.clear()
    self.write(f"SCORE: {self.score}    HIGH SCORE: {self.high_score}", False, align=ALIGNMENT ,font=FONT)
  
  def increment(self):
    self.score += 1
    if self.score > self.high_score:
      self.high_score = self.score
    self.update_scoreboard()
  
  def reset(self):
    self.score = 0
    self.update_scoreboard()