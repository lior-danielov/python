# list
# my_list = [1, 2, 3]

# tuples
# my_tuple = (1, 3, 8)

# tuples are immutable

# import turtle as t
# import random
#
# tim = t.Turtle()

# event listeners

# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
# screen.listen()
#bind
#keystroke
#event


# def move_forwards():
#     tim.forward(10)


# screen.onkey(key="space", fun=move_forwards)
# screen.exitonclick()
#
# def function_a(something):
    # do this with something
    # then, do this
    # finally, do that

# def function_b():
    # do something_new

# function_a(function_b())

# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# def calculator(n1, n2, func):
#     return func(n1, n2)
#
#
# result = calculator(2, 3, divide)
# print(result)
# higher order functions

# for number in range(1, 101):
#     if number % 7 == 0 or number / 7 == 0:
#         print("b")
#     if number % 7 == 0:
#         print("7")
#     if number / 5 == 0:
#         print("b")
#     else:
#         print([number])
#
# Object State and Instances
# Turtle Coordinate System

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)  # override
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win? (enter a color): ")
print(user_bet)


screen.exitonclick()
# w  קדימה
# d ימינהa שמאלהs אחורה

