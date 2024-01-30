from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money = MoneyMachine()
maker1 = MenuItem(name="lattte", water=200, milk=150, coffee=24, cost=2.5)
maker = Menu()

maker.get_items()
condition_to_make = CoffeeMaker()
ingredients = ("water", 100)
condition_to_make.make_coffee(order=16)