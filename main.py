from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()                           # generating a screen object
screen.setup(width=800, height=600)         # adjusting the dimensions of the screen object
screen.bgcolor("black")                     # adjusting the color of the screen object
screen.title("Pong")                        # choosing the title of the screen object
screen.tracer(0)                            # disabling the tracer function for smoother performance

scoreboard = Scoreboard()                   # creation of a scoreboard object
r_paddle = Paddle((350, 0))                 # creation of a right paddle object using the paddle class and coordinates
l_paddle = Paddle((-350, 0))                # creation of a left paddle object using the paddle class and coordinates
ball = Ball()                               # creation of a ball object

screen.listen()                             # using the listen method to allow keyboard presses to affect the game
screen.onkey(r_paddle.go_up, "Up")     # using onkey method to assign right peddle go up method to the up key
screen.onkey(r_paddle.go_down, "Down") # using onkey method to assign right peddle go down method to the down key
screen.onkey(l_paddle.go_up, "w")       # using onkey method to assign left peddle go up method to the w key
screen.onkey(l_paddle.go_down, "s")     # using onkey method to assign left peddle go up method to the s key

game_is_on = True                           # the game on variable for the while loop

while game_is_on:
    screen.update()                         # calling the update method to refresh the screen in every iteration
    time.sleep(ball.decrease_move_speed)             # using the sleep method to control increase the refresh rate
    ball.move_ball()                        # calling the move method to start ball movement
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Detect R pedal miss
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()

    # Detect L pedal miss
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()

    if scoreboard.r_score == scoreboard.target_score or scoreboard.l_score == scoreboard.target_score:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
