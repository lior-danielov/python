'''

choose the first number - 2
choose the second operand - 3
choose the operator (+,-,/,*)  --> *
use print (f...)
every operator must be coded into its own function
End of calculator program>
'''

num1 = int(input("enter number one: "))
operand = (input("enter operand: "))
num2 = int(input("enter number one: "))
def addition(num1 , num2):
    return num1 + num2
def subtract(num1 ,num2):
    return num1 - num2
def multiplication(num1 ,num2):
    return multiplication(num1 * num2)
def division(num1 ,num2):
    return num1 * num2
if operand == '+':
    res = addition(num1, num2)
if subtract == '-':
    res = num1, num2
if multiplication == '*':
    res = num1, num2
if division == '/':
    res = num1, num2
print(res)
'''

res = 3 +4 * 233 / 33  #(compound expression --> process -> literal)
add_func(2, 3)
mult_result = add_func(2, 3)
res = len("hi")
print(res)


def sayBy():
    return
print(sayBy)
'''
