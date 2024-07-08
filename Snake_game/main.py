from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard
screen = Screen()
screen.setup(width=580, height=595)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
start_pos = [(0, 0), (-20, 0), (-40, 0)]

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # collision with food

    if snake.head.distance(food) < 15:   # Adjust the value according to your game design

        food.respawn()
        snake.extends()
        screen.update()
        scoreboard.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    for i in snake.heads[1:]:
        if snake.head.distance(i) < 10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()
