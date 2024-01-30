import random
import guess_graphic
pc_num = random.randint(0, 100)
print(guess_graphic.welcome)
choose_level = input("choose hard or easy (h/e): ")
guess_num = int(input("enter your wright number: "))
def check():
    if 100 >= guess_num >= 1:
        if guess_num == pc_num:
            print("You win!")
        elif guess_num < pc_num:
            for i in range(num_guesses):
                print("Too low")
        else:
            for i in range(num_guesses):
                print("Too high")
    else:
        print(f"You are not successes ,The number was: {pc_num}")

if choose_level == "h":
    num_guesses = 5
    for i in range(num_guesses):
        check()
elif choose_level == "e":
    num_guesses = 10
    for i in range(num_guesses):
        check()
else:
    print("Please choose again...")
print("Game over.sorry only in kipper day")
'''
#globals
# def chek(g,n,m)
# def level()
# s =  input()
# level(s)
# while m > 0
# input
# check (g,n,m)
'''