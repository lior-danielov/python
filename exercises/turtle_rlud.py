from turtle import *

# create the turtle
pencle = Turtle()
screen = Screen()

'''
tim = Turtle()
tim.shape(turtle)
tim.shapesize(turtle)
# tim.pencolor() = tim1
'''
def come_on():
    pencle.forward(10)


def back_on():
    pencle.backward(10)


def go_left():
    pencle.left(10)


def go_right():
    pencle.right(10)


def clear():
    pencle.clear()


screen.listen()
#press on keys
screen.onkey(key="w", fun=come_on)
screen.onkey(key="s", fun=back_on)
screen.onkey(key="a", fun=go_left)
screen.onkey(key="d", fun=go_right)
screen.onkey(key="x", fun=clear)

screen.mainloop()