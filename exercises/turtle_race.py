from turtle import Turtle, Screen
from random import randint

# create the turtle
tim = Turtle()
screen = Screen()
list_turtle = []
screen.setup(width=500, height=400)  # override
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win? (enter a color): ")
print(user_bet)
colors = ["red", "green", "blue"]
y_index = [-70, -10, 50]

for turtle_index in range (0,3):
    tim = Turtle(shape = "turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230,y=y_index[turtle_index])
    tim.pendown()
    list_turtle.append(tim)
flag = 1
while flag:
    for tim in list_turtle:
        dist = randint(1, 10)
        tim.forward(dist)

        if tim.xcor() > 230:
            win = tim
            flag = 0
            break
if user_bet == colors.index(win.color()[0]):
    print("you winner")
else:
    print("try again ...")

turtle.done()
'''
def turtle_goto():
    tim1 = tim.pencolor(x = 230)
'''
# tim.pencolor() = tim1
turtle_index()

screen.exitonclick()
