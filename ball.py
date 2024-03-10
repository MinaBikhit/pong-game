from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")        # choosing the turtle shape as circle
        self.color("white")         # choosing color for the ball class
        self.penup()                # penup to avoid line drawing by turtle
        self.speed(0)               # adjusting the speed to zero (fastest) for loading ball
        self.x_move = 10            # defining the rate of change in the x-axis (along with y-move changes the direction of the ball)
        self.y_move = 10            # defining the rate of change in the y-axis (along with x-move changes the direction of the ball)
        self.decrease_move_speed = 0.1       # defining the speed of the ball (to be reused as sleep time in main.py)

    def move_ball(self):
        """method that is used to change the position of the ball by the values set for x_move and y_move"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        """method that simulates the bounce by multiplying the x_move by a negative factor and also increases the game speed by redusing the decrease in move speed"""
        self.x_move *= -1
        self.decrease_move_speed *= 0.9

    def bounce_y(self):
        """method that simulates the bounce by multiplying the x_move by a negative factor"""
        self.y_move *= -1

    def reset_ball(self):
        """method that resets the ball to the center of the board while reversing the direction of movement"""
        self.x_move = -1
        self.decrease_move_speed = 0.1
        self.home()
