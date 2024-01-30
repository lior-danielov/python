# Shadowing
# enemies = 1
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# DON'T shadow if you can... or else...

# enemies = 1
#
# def increase_enemies():
#     enemies = 1 # sol.
# enemies += 2 # enemies = enemies + 2
# print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()


# enemies = 1

# def increase_enemies():
#     global enemies # listen to me... it's the same! don't be fooled!
#     global enemies += 2 # enemies = enemies + 2
# enemies += 2
# print(f"enemies inside function: {enemies}")


# increase_enemies()
# AVOID GLOBALS WHENEVER POSSIBLE!

# try: make the function call to inc. enemies by 2
# sol:
# enemies = 1
# def increase_enemies():
#     return enemies + 2
#
# enemies = increase_enemies()
# print(f"enemies outside func.: {enemies}")

# guessing game
'''
Welcome to the guessing game!
I'm thinking of a number between 1-100
choose difficulty: type 'easy' or 'hard'

---> hard
You have 5 attempts remaining to guess the game
--> guess > number --> "too high. guess again"
--> guess < number --> "too low. guess again"
--> guess is the number --> "Yes!"

--> every mistake? "you have 4 tries...3 2 1   game over you lose
the number was: ...

---> easy --> 10 tries

NOTES
* must use constants (file "globals")
* don't use shadowing
* use the return command in a correct way
* must document every function you write
* must use functions
* must use graphics
* must divide and conquer (use modules)
* date of submission: not later than 08.11 (0100 am)
* link to a working OnlineGDB code
<END OF GUESSING GAME PROJECT>
------------------------------------------------------
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
--> choose a beverage (latte, cappuccino, espresso)
--> e.g., Latte  --> insert money  --> "how many pennies to insert? how many Nickels...?
--> if exact: the amount of money you inserted is enough.
    {will check for resources}
    if there are enough resources --> "here is your latte"
    if the amount inserted is > than needed --> the machine will check its internal tanks
    here is your change: ...
---> technician mode  ---> passcode ("1234")

SRD
SRS

* Correct logic, cover ALL of the requirements
* graphics
* documentation/comments
* divide and conquer
* technical documents (SRD, SRS)
* more than 50 lines of code
* until Sunday, at 0100 (morning).
'''

# TODO: 1. Check for sufficient resources.

# TODO: 2. Ask the user what he wants.
