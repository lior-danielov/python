from random import randint
import pytz

from turtle import *
x = 10
y = 3
timmy = Turtle()
screen = colormode(255)
for i in range(1, 7):
    for y in range(3, 12):
        x = x + 10
        y += 1
        timmy.circle(x, None, y)
        timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))
    y = 3
    x = 10
    timmy.right(60)
    pensize(randint(215))


screen = Screen()
screen.exitonclick()
