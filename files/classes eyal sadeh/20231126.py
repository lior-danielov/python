# String Formatting (uses string replacement fields)
# {} - string interpolation
# for i in range(1, 13):
#     print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i**2, i**3))

# field width
# align to the left
# ^ ==> center
# string replacement field / string placeholder
# string interpolation
# ** = exponent

# print("Pi is approximately {0:12}".format(22 / 7))
# print("Pi is approximately {0:12f}".format(22 / 7))
# print("Pi is approximately {0:12.50f}".format(22 / 7))
# print("Pi is approximately {0:52.50f}".format(22 / 7))
# print("Pi is approximately {0:^62.50f}".format(22 / 7))
# print("Pi is approximately {0:<72.50f}".format(22 / 7))  # align to the left (<)

# for i in range(1, 13):
#     print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))
# print("Pi is approximately {0:12f}".format(22 / 7))

# num = 2
# print(4/3)

# basic python string interpolation
# age = 24.3
# print("My age is %.1f years" % age)

# major = "years"
# minor = "months"
# print("My age is %d %s, %d %s" % (int(age)/10, major, 6, minor))  # respectively

# in and not in

# parrot = "Norwegian Blue"
# letter = input("Enter a character: ")
#
# if letter in parrot:
#     print("{} is in {}".format(letter, parrot))
# else:
#     print("I don't know that letter.")
#
# activity = input("What would you like to do today? ")
#
# if "cinema" not in activity.casefold():  # best practice
#     print("But I wanna go to the cinema!")

# LISTS

# numbers = [1, 2, 3, 4, 5]
# my_list = [1, 2, 3]
my_list = ['string', 100, 100.23]

# print(len(my_list))
# print(my_list[1:])
another_list = ["two", "3"]

new_list = my_list + another_list
# print(new_list)

lll = [new_list[0]]
# print(type(lll))

# new_list[0] = ['ONE ALL CAPS']
# new_list.append(5)
# print(f"before: {new_list}") # F-strings ("printf")
# strange = new_list.pop()
# print("Popped value: %s" % strange)  # (basic) string interpolation
# print("new list: {}".format(new_list)) # string formatting
# print(new_list.pop(2))  # pop is a destructive method, beware!
# print(new_list.append(2)) # Big no-no

# listt = [1, 3, 2.33]
# listt.sort()  # 1, 2. ,3
#
# listt.reverse()
# print(listt)

# Dictionaries
# key-value pairing

# my_dict = {'key1': 'value1', 'key2': 'value2'}
# print(my_dict['key1'])

# prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}

# d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': 100}}
# print(d['k2'])
# print(d['k3'])
# print(d['k2'][2])
# print(d['k3']['insideKey'])
# d = {'key1': ['a', 'b', 'c', 'd'], 'key2': 'rara'}
# print(d['key1'][2].upper())
# mylist = d['key1']
# print(mylist)
# d['key1'][2] = 'e'
# print(d)
# print(d.keys())
# print(d.values())
# d = {'key1': ['a', 'b', 'c', 'd'], 'key2': 'rara'}
# print(d.items())
# print(d)

# tuples are immutable
# my_tuple = (1, 2, 3)
# t = ('one', 2)

# print(type(t))
# print(t[-1])
t = ('a', 'b', 'a', 'd')
# print(t.count('a'))
print(t.index('a'))
