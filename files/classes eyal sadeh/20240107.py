import re

#   ^  caret sign  -> the start of the str
#   $  dollar sign -> the end of the string

# pattern = r'world$'
# text_string = "Hello World"
# text_string = "Hello dsfsdf dsafsdfds dsfsdfdsfsd world"

# if re.search(pattern, text_string):
#     print(f"{text_string} ends with 'world'")
# else:
#     print(f"{text_string} does not end with 'world'")

# pattern = r'^hello'
# test_string = ['hello world', ' hello123', 'world hello', 'hi there']

# for string in test_string:
#     if re.match(pattern, string):
#         print(f"{string} starts with 'hello'")
#     else:
#         print(f"{string} does not start with 'hello'")

# match-case

# value = 42
#
# match value:
#     case:
#         print("It's a zero")
#     case 42:
#         print("The answer to the meaning of life...")
#     case _:  # wildcard
#         print("Something else")
# Write a program which classifies a grade
# 50 -> fail , 60 -> pass, 70 -> OK, 80 -> good, 90 -> very good , 100 -> excellent

# value = 42
# match value:
#     case x if x % 2 == 0:
#         print("OK")
# possible, but I don't like it

# assert (...tomorrow)







