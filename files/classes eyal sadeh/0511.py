'''
Welcome to the cypher program

{logo}

Choose what would you like to do:
Encrypt (press 1)
decrypt (press 2)

---> 1
input -->"Hello"
OK, enter the offset >>>
input --> 2
Encrypted sentence: Jgnnq
Would you like to continue or quit? (C or Q)

--- 2
OK, enter the encrypted sentence >>> jgnnq
Enter the offset >>> -2
Decrypted sentence: Hello
Would you like to continue or quit? (C or Q)

# if the user chooses to quit, then the program exists. else, the screen will clear
and he will start over.


# find the ASCII value of a given character
# char = 'p'
# print("The ASCII value of " + char + " is ", ord(char))

# print(chr(97))

# additional requirement:
# if the user, for example, writes: 'zzz' and +1 then --> 'aaa'
# Same with upper-case letters!  (Z+1=A)

<END of Ceasar-Cypher Assignment>
'''


 # def add_func(a, b):
 #     return a * b
 #     print("bye")  # DEAD CODE :-(

# res = 3 +4 * 233 / 33  (compound expression --> process -> literal)
# add_func(2, 3)
# mult_result = add_func(2, 3)
# print(result)

# res = len("hi")
# def sayBy():
#     return
#
# print(sayBy)

# Write a function which gets a sentence from the user,  and converts it to
# title case (where each 1st letter is in upper-case
# e.g., hello sir  --> Hello Sir

# option 1:
# def upperTheSen(in_str):
#     return in_str.title()
#
#
# str = input("Enter something >>> ")
# res = upperTheSen(str)
#
# print(res)

# for Tuesday (before the lesson): The Calculator
'''
Hello, and welcome to the calculator!
{logo}
choose the first operand  --> 2
choose the second operand --> 3
choose the operator (+,-,*,/) --> *
The result of 2 * 3 is: 6  
* use print(f...)
* every operator must be coded into its own function
<END of Calculator program>
'''


# scope

# local scope example
# enemies = 1
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# def drink_potion():
#     potion_strenth = 1
#
# print(potion_strenth)
# drink_potion()

# global scope

# player_health = 10  # "global" variable
#
# def print_health():
#     print(player_health)

# player_health = 10
# def game():
#     def drink_potion():
#         potion_strenth = 2
#         print(player_health)
#
# drink_potion()

# block scope (not in Python!... )
# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0]
# print(new_enemy)

# WILL THIS WORK?!
game_level = 3
def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]  # local ONLY to the function
print(new_enemy)

