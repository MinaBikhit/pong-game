from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position                    # position used in the initialization of the paddle object
        self.shape("square")                        # choosing the turtle shape as square
        self.shapesize(stretch_wid=5, stretch_len=1)   # resizing the paddle object
        self.color("white")                             # choosing color for the paddle object
        self.penup()                                    # penup to avoid line drawing by turtle
        self.goto(position)                             #setting the initial position of the paddle based on the tuple inputed during object creation
        self.speed(0)                                   # adjusting the speed to zero (fastest) for loading Paddle

    def go_up(self):
        """method to move the paddle up within the borders of the screen"""
        if self.ycor() < 245:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        """method to move the paddle down within the borders of the screen"""
        if self.ycor() > -235:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
