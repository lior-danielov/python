"""

def squrt(a, b):
    res = 0
    while a >= b:
        res += 1
        a -= b
    return res


result = squrt(9, 3)  # 5
print(result)




def next_letter(letter):
    if 96 <= ord(letter) <= 122:
        return chr(ord(letter) + 1)

def next_str(str):
    a = ""
    if 96 <= ord(str) <= 123:
        for i in str:
            a += next_letter(i)
        return a


print(next_letter("a"))
print(next_str("ab"))

"""

import math
def calculate_sum_in_base_3(num):
    total = 0
    p = 0
    for digit in reversed(num):
        digit = int(digit)
        term_result = digit * math.pow(3, p)
        print(f"{digit} * 3^{p} = {term_result}")
        total = total + term_result
        p = p + 1

    return total
input_number = '11012'

result = calculate_sum_in_base_3(input_number)

print(f"Total sum for {input_number} in base-3 is: {result}")
