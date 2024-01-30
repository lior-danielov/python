'''
# COFFEE MACHINE
IDE - Integrated Development Environment
Linter - an intelligent system which checks our code in real time

GTD203

COIN TYPES:
penny = 1 cent (0.01$)
Nickel = 5 cent (0.05$)
Dime = 10 cent (0.1$)
Quarter = 25 cent (0.25$)

* The machine will be able to print a report (how much money of each type is inside
  + how much is left of every resource)
'''

'''
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "money": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "money": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "money": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
        "espresso":{
        {
        "penny": 0.01,
        "Nickel": 0.05,
        "Dime": 0.1,
        "Quarter": 0.25
        }
    },
        "late":{
        {
        "penny": 0.01,
        "Nickel": 0.05,
        "Dime": 0.1,
        "Quarter": 0.25
        },
    },
        "espresso":{
        {
        "penny": 0.01,
        "Nickel": 0.05,
        "Dime": 0.1,
        "Quarter": 0.25
        },
    }
}
--> choose a beverage (latte, cappuccino, espresso)

choose_beverage = input("please insert what you want: latte cappuccino espresso")
choose_type_of_money = input("insert money please: pennies, nickels, Dimes, Quarters: ")
amount_of_money = int(input("please enter amount of money: "))
def check_price_coffee_M():
  if choose_beverage == "latte":
    for i in range(amount_of_money):
      if choose_type_of_money == "p" :
        amount_of_money
check_price_coffee_M()

if money["late"] == check_price_coffee_M():


'''
'''
נ.ב לכתוב תפריט של סוג הכספים ומספרן לפי הבן אדם שמכניס את הכסף לבנות את התנאי האם יש מספיק כסף לקפה
אם כן תוציא קפה אם לא תכתוב צריך עוד כסף או שהעסקה בוטלה

if resources == amount_of_money:
    print("your coffe is created...")

--> e.g., Latte  --> insert money  --> "how many pennies to insert? how many Nickels...?
--> if exact: the amount of money you inserted is enough.
    {will check for resources}
    
import graphic_coffee_machine

money_inside = 0
latte_price = 2.5
cappuccino_price = 3
espresso_price = 1.5

coffee_machine_tank = {
    "milk": 10000,
    "water": 10000,
    "coffee": 1000,
    "price": 1000
}

def choose_coffee():
    choose_beverage = input("please insert what you want: latte cappuccino espresso")
    if choose_beverage == "e":
        price_cofe = espresso_price
    elif choose_beverage == "c":
        price_cofe = cappuccino_price
    elif choose_beverage == "l":
        price_cofe = latte_price
    elif choose_beverage == "owner":
        owner_machine()
        return None, 0
    else:
        print("Please choose a correct code")
        return None, 0
    return choose_beverage, price_cofe


def down_coffee(choose_kind):
    # Add logic to decrease resources based on the chosen coffee type
    pass


def insert_money(price_cofe):
    total_price = 0
    while total_price < price_cofe:
        choose_coin = input("Please enter the code for the coin you want to insert (p/n/d/q): ")
        if choose_coin == "p":
            total_price += 0.01
        elif choose_coin == "n":
            total_price += 0.05
        elif choose_coin == "d":
            total_price += 0.1
        elif choose_coin == "q":
            total_price += 0.25
        else:
            print("Please insert a valid coin.")
        print(f"The total price you have inserted is: {total_price}")
    coffee_machine_tank["price"] += total_price
    print("Thank you! Enjoy your coffee.")


def report_machine():
    print("Coffee Machine Report:")
    print(coffee_machine_tank)


def owner_machine():
    report_machine()
    add_or_not = input("Do you want to add something? (y/n): ")
    if add_or_not == "n":
        print("Ok, have a good day!")
        main_machine()
    elif add_or_not == "y":
        coffee_machine_tank["milk"] += int(input("Please add milk: "))
        coffee_machine_tank["water"] += int(input("Please add water: "))
        coffee_machine_tank["coffee"] += int(input("Please add coffee: "))
        take_money = input("Do you want to take money? (y/n): ")
        if take_money == "n":
            print("Ok, have a good day!")
            main_machine()
        elif take_money == "y":
            print(f"The machine has ${coffee_machine_tank['price']}")
            coffee_machine_tank['price'] -= int(input("How much do you want to take? "))
            print("Ok, have a good day!")


def main_machine():
    print("Welcome to the coffee machine!")
    choose_beverage, price_cofe = choose_coffee()
    if choose_beverage:
        down_coffee(choose_beverage)
        insert_money(price_cofe)


print(graphic_coffee_machine.welcome)
main_machine()

    if there are enough resources --> "here is your latte"
    if the amount inserted is > than needed --> the machine will check its internal tanks
    here is your change: ...
---> technician mode  ---> passcode ("1234")

SRD
SRS

* Correct logic, cover ALL the requirements
* graphics
* documentation/comments
* divide and conquer
* technical documents (SRD, SRS)
* more than 50 lines of code
* until Sunday, at 0100 (morning).
'''
from prettytable import PrettyTable
table = PrettyֻTable()