def say_hello(name, age):
    print(f"Hello {name}, you are {age} years old.")

x = input("Say your name: ")
y = input("Say your age: ")

say_hello(y, x)


#keyword-arguments - examples and problems
def func(a, b, c):
    print(a)
#ex.
func(2,1,3) #2
func(b=2, a=1, c=3)#1

#conditions for using both positional-args. and keyword-args. combined:
#a. first use pos., and only then - keyword
#b. no duplicates are allowed
#ex. func(3,2,c=1)

#Exercise: Write a func. which gets a number from the user and prints whether it's a prime.

def prime_check(num1):
    is_prime = True
    for i in range(2, num1):
        if num1 % i == 0:\
    is_prime = False

    if not is_prime:
        print(f"{num1} is not a prime number")
    else:
        print(f"{num1} is a prime number")

    num = int(input("Enter a number: "))
prime_check(num1)

#hangman - game_flow
