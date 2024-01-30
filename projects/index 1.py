# def func(value):
#     sum1 = []
#     sum2 = []
#     for i in value:
#         sum1.append(i)
#     for j in range(i, len(value)):
#         sum2.append(j)
#     if sum1 == sum2:
#         print(sum1)
#     else:
#         print("False")
"""
def func(val):
    for index in range(len(val)):
        if sum(val[:index+1]) == sum(val[index+1:]):
            print(f"index is: {val}, the value is: {val[index]}")
            return True
    return False


print(func([1, 2, 3]))

"""

"""
def func(val):
    length = len(val)
    for i in range(length - 1):
        for j in range(length - i -1):
            if val[j] < val[j + 1]:
                val[j], val[j + 1] = val[j + 1], val[j]

    my_list = val
    new_list = map(str, my_list)
    string_value = ''.join(new_list)
    number = int(string_value)
    print(number)

arr = [1, 2, 3]
func(arr)

# """
# import random
#
#
# def func():
#     # res = (ord(random.random(chr("A"), chr("Z")))
#     str = input("please enter string")
#     res = []
#     res1 = ""
#     for i in str:
#         if i.isupper():
#             res.append(i)
#     for _ in range(len(str)):
#        res1 += random.choice(res)
#     print(res1)
#
#
# func()
"""
def print_all_mpn_numbers(n):
special_numbers = []
num = 1

while len(special_numbers) < n:
if is_special_number(num):
special_numbers.append(num)
num += 1
print(special_numbers)

n = int(input("How many MPN would you like to print? >>> ") )
print_all_mpn_numbers(n)
"""


def colzhut(n):
    mas_a, mas_b = 7010, 10060  # (10%, 14%) 20%,16150, 31% 22440 , 35% 46690 ,47% 60130 50% > 60130
    mas_c, mas_d, mas_e = 16150, 22440, 46690
    mas_f = 60130
    mastot = 0
    mas_exa = mas_a * (10/100) + (n - mas_a) * (14 / 100) + (n - mas_b) * (20 / 100) + (n - mas_c) * (31 / 100)

    if n < mas_a:
        mastot = n * (10/100)
    elif n < mas_b:
        mastot = mas_a * (10/100) + (n - mas_a) * (14 / 100)
    elif n < mas_c:
        mastot = mas_a * (10/100) + (n - mas_a) * (14 / 100) + (n - mas_b) * (20 / 100)
    elif n < mas_d:
        mastot = mas_a * (10/100) + (n - mas_a) * (14 / 100) + (n - mas_b) * (20 / 100) + (n - mas_c) * (31 / 100)
    elif n < mas_e:
        mastot = mas_exa + (n - mas_d) * (35 /100)
    elif n < mas_f:
        mastot = mas_exa + (n - mas_d) * (35 /100) + (n - mas_e) * (47 / 100)
    else:
        mastot = mas_exa + (n - mas_d) * (35 /100) + (n - mas_e) * (47 / 100) + (n - mas_f) * 0.5

    return mastot


print(colzhut(75000))