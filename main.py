import turtle
import time
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard
from ui import UI

screen=turtle.Screen()
screen.setup(width=1000,height=600)
screen.bgcolor("black")
screen.title("80's Game")
screen.tracer(0)

paddle=Paddle()
ball=Ball()
bricks = Bricks()
scoreboard=Scoreboard()
ui=UI()

game_is_on=True
game_paused = False


def pause_game():
    global game_paused

    if game_paused:
        game_paused = False
    else:
        game_paused = True
        time.sleep(10)


def start_game():
    global game_is_on

    while game_is_on:
        if not game_paused:
            screen.update()
            time.sleep(ball.speed_move)

            ball.move()
            ui.white_txt()

            screen.listen()
            screen.onkey(paddle.move_left,"Left")
            screen.onkey(paddle.move_right,"Right")
            screen.onkey(pause_game, "space")

            if ball.ycor() > 270:
                ball.bounce_y()
                ball.speed_up()

            if ball.xcor() > 470 or ball.xcor() < -470:
                ball.bounce_x()
                ball.speed_up()

            if ball.ycor() < -300:
                ui.game_over()
                scoreboard.save_high_score()
                game_is_on=False

            if ball.distance(paddle) < 100 and ball.ycor() < -220:
                ball.bounce_y()
                ball.speed_up()

            for brick in bricks.all_bricks:
                if ball.distance(brick) < 37:
                    brick.quality -= 1
                    if brick.quality == 0:
                        brick.goto(1984,1984)  #brick will disappear
                        scoreboard.update_scoreboard()
                        bricks.all_bricks.remove(brick)

                        if len(bricks.all_bricks)==0:
                            ui.declare_win()
                            scoreboard.save_high_score()
                            game_is_on = False

                    # detect collision from left or right edge of brick
                    if ball.distance(brick) < 15:
                        ball.bounce_x()
                    # detect collision from bottom or top edge of the brick
                    elif ball.distance(brick) < 30:
                        ball.bounce_y()
        else:
            pause_game()


user_response=screen.textinput(title="Start Game",prompt="Do you wanna play the game? [Yes/No]")

if user_response.lower()=="yes":
    start_game()
else:
    screen.bye()

screen.mainloop()