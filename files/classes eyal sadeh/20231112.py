'''
OOP - Object Oriented Programming
תמ"ע

attributes
methods

methods vs functions

מופע = instance = אדגום (דגם)
לאדגם = למפע
occurrence

blueprint

class = (reference) type  = מחלקה / טיפוס מורכב

Classes will be written in PascalCase

car = CarBlueprint()
here we instantiated a "CarBlueprint" object (variable) named "car"

every class has a "constructor"

Turtle Graphics

Dot Object Notation


# import turtle
# timmy = turtle.Turtle()

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")


my_screen = Screen()
my_screen.exitonclick()
--------------------------

PyPi
Prettytable

from prettytable import PrettyTable

table = PrettyTable()

HW:
create a table with 3 Pokemon names and their types. use the following data:
Headers:
Pokemon Name
Type


Names: Pikachu, Squirtle, Charmander
Type: Electric, Water, Fire

from turtle import Turtle, Screen
from prettytable import PrettyTable

table = PrettyTable(["headers: ", "pokemon name: ", "type: "])
table.add_row(["big pokemon", "picatu", "elctro"])
table.add_row(["iron", "magneto", "water"])
table.add_row(["gooder else", "batman", "spider"])
print(table)
my_screen = Screen()
my_screen.exitonclick()
'''
import random
from turtle import * #Turtle, Screen
from random import *

timmy = Turtle()
screen = colormode(255)
choose = "right" or "left"
x = 3
while True:
    move = randint(1, 3)
    if move == 1:
        timmy.forward(randint(1, 10))
        timmy.right(90)
    elif move == 2:
        timmy.forward(50)
        timmy.left(90)
    else:
        timmy.forward(50)
    timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))
    x += 1

screen = Screen()
screen.exitonclick()
