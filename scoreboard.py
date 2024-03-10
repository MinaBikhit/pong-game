from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, 'normal')
FONT_GAME_OVER = ("Courier", 24, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")         # defining text color as white
        self.penup()                # using penup to avoid drawing lines by the turtle
        self.hideturtle()           # hiding the turtle symbol
        self.l_score = 0            # score variable for the left paddle  initialized at zero
        self.r_score = 0            # score variable for the right paddle  initialized at zero
        self.update_score()         # calling the update_score method to initially display the score when the object is created
        self.target_score = 10      # score target value for wining

    def update_score(self):
        """method that writes the score in the screen"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        """method that increases the score """
        self.l_score +=1
        self.update_score()

    def r_point(self):
        """method that increases the score """
        self.r_score += 1
        self.update_score()

    def game_over(self):
        """method that displays Game Over when a player wins"""
        self.home()
        if self.l_score == self.target_score:
            self.write("Game Over! \nLeft Player Won!!", True, align=ALIGNMENT, font=FONT_GAME_OVER)
        elif self.r_score == self.target_score:
            self.write("Game Over! \nRight Player Won!!", True, align=ALIGNMENT, font=FONT_GAME_OVER)