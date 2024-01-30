# tuples are immutable
# my_tuple = (1, 2, 3)
# t = ('one', 2)

# print(type(t))
# print(t[-1])
# t = ('a', 'b', 'a', 'd')
# print(t.count('a'))
# print(t.index('a'))

# Unpacking a Tuple
# a = b = c= d = e = f = 12 # shorthand assignment
# c = 22
# print(d)
#
# a = "srer"
# b = a
# a = "sss"
# print(b)

# x, y, z = 1, 2, 76
# print(x)
# print(y)
# print(z)

# print("Unpacking a tuple")
# data = 1, 2, 76  # data represents a tuple
# print(type(data))
# x, y, z = data
# print(x)
# print(y)
# print(z)

# tuples are immutable

# print("Unpacking a list")
# data_list = [12, 13, 14]
# data_list.append(15)  # NO NO!!!
# p, q, r = data_list
# print(q)
# print(p)
# print(r)


# for i in "abfffd":
#     print(i)

# enumeration
# for index, character in enumerate("abcdefgh"):  # also unpacks the tuple
#     print(index, character)

# names = ["Alice", "Bob", "Charlie"]
# for index, name in enumerate(names):
#     print(f"{index + 1}. {name}")  # the tuples were unpacked

# for tutian in enumerate("abcdefgh"):
#     print(tutian)  # will show us tuples

#for t in enumerate("abcdefgh"):
 #   index, character = t  # unpacking the tuple...
  #  print(index, character)
'''
class User:
    def __init__(self, userID, username):
        self.id = userID
        self.username = username
        # default values
        self.followers = 0
        self.following = 0

    def follow(self, whats_his_name):
        self.following += 1
        whats_his_name.followers += 1


user_1_chaim = User("1234", "Chaim")
user_2_ben = User("5678", "Benayahu")

user_2_ben.follow(user_1_chaim)
print(user_2_ben.following)
print(user_1_chaim.followers)
'''
'''

res = [1,3,5,2,7,2,3]
res.append(27)
myset = set(res)
myset.add(27)
print(myset)

'''
# with open("my_file.txt", mode="w") as file:
#     contacts = file.write("hi ny name is ...")
#
# with open("my_file.txt", mode="a+") as file:
#     contacts = file.write("hi ")
#
# with open("my_file.txt") as file:
#     contacts = file.read()
#     print(contacts)
istuple = ("apple", "saa", 221)
res = enumerate(istuple)
for i, x in enumerate (istuple):
    print(i, x)