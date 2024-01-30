# age = int(input("Enter your age >>> "))

# using assert to check if the age variable is greater than or equals 18
# assert age >= 18, "You must be 18 or older!"

# if we reached this line, then life continues...
# print("You may play the game of life...")

# if the assert fails, an AssertionError is raised, and the program halts.


# age = int(input("Enter your age >>> "))

# def divide(x, y):
#     assert y != 0, "Cannot divide by zero!"
#     return x / y


# result = divide(10, 2)  # Works as expected
# result = divide(10, 0)  # Raises an AssertionError
# print(result)

# def calculate_area(length, width):
#     assert isinstance(length, (int, float)), "Length must be a number!"
#     assert isinstance(width, (int, float)), "Width must be a number!"
#     return length * width


# area = calculate_area(5, 3)    # as expected
# area = calculate_area("5", 3)  # Raises AssertionError
# print(area)
# print("Tal: I've been a bad boy\n" * 10)

# def withdraw_money(account, amount):
#     assert account.balance >= amount, "Sorry, not enough money. go to work..."
#     account.balance -= amount
# more code to manipulate account balance, and logs
# assert account.balance >= 0, "Account balance cannot be negative!"

'''
Homework - ASSERTION (knas: 100 Pts.)
Write a program that simulates a bank account with deposit and withdraw methods. add assertions
to insure that the balance is always >=0, and that the user cannot deposit more than 5000 a day,
and also, cannot withdraw more than 5000 a day.

Or, write your own story...
'''
# print("H1")
#
#
# def yoelFunction():
#     print("This func. can be called from anywhere!")
#
#
# if __name__ == "__main__":
#     print("this code only runs when the file is the main program.")
#     yoelFunction()
#
#
# print("H2")


# Big-O Notation

# example for O(sqrt(n))
def sqrt_test(n):
    if n < 0:
        raise ValueError("cannot be less than 0")

    if n == 0 or n == 1:
        return n

    # approximation
    x = n
    y = 1

    while x > y:
        x = (x + y) // 2
        y = n // x

    return x

#ex
num = 23
print(sqrt_test(num))




