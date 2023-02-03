from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Bada Bing Bada Pong")
screen.tracer(0)

player1_paddle = Paddle(-350, 0)
player2_paddle = Paddle(350, 0)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player1_paddle.up, "w")
screen.onkeypress(player1_paddle.down, "s")
screen.onkeypress(player2_paddle.up, "Up")
screen.onkeypress(player2_paddle.down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.1)

    # collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with paddle
    if (ball.distance(player2_paddle) < 50 and ball.xcor() > 320) or (ball.distance(player1_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # out of bounds
    if ball.distance(player2_paddle) > 50 and ball.xcor() > 400:
        ball.reset()
        ball.bounce_x()
        scoreboard.l_point()
        scoreboard.update_scoreboard()

    if ball.distance(player1_paddle) > 50 and ball.xcor() < -400:
        ball.reset()
        ball.bounce_x()
        scoreboard.r_point()
        scoreboard.update_scoreboard()

screen.exitonclick()
