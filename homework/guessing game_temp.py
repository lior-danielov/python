'''
Welcome to the guessing game!
I'm thinking of a number between 1-100
choose difficulty: type 'easy' or 'hard'
'''
import random
choose_number = random.randint(1, 100)
choose_hard_or_easy = int(input("chose press 1 to hard or  0 for easy: "))
guess_num_effective = int(input("choose number effective: "))
guess = "You 5 attempts remaining to guess the game: "
too_high = "too high. guess again"
too_low = "too low. guess again"
high_level = 5
low_level = 10
every_mistake = "you have more : "
def forloop():
    for i in range(high_level, 0, -1):
        print(i)
    for i in range(low_level,0, -1):
        print(i)
forloop()
def condition():
    if guess_num_effective < choose_number:
        print(f"{too_low} , {every_mistake} , {forloop()}")
    elif guess_num_effective > choose_number:
        print(f"{too_high} , {every_mistake} , {forloop()}")
    else:
        print("you win")
condition()
'''
---> hard
You have 5 attempts remaining to guess the game
--> guess > number --> "too high. guess again"
--> guess < number --> "too low. guess again"
--> guess is the number --> "Yes!"
'''
def condition2():
    if choose_hard_or_easy == 1:
        for i in range(high_level, 0,-1):
            print()
    elif choose_hard_or_easy == 0:
        for i in range(low_level, 0, -1):
            condition()
    else:
        print("mistake in the press...")
condition2()
'''
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
'''