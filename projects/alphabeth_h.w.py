import re


def func(word):
    explain = r"^[A-Za-z0-9]*[A-Za-z0-9()_-]*\.(gif|png|jpeg|jpg)$"
    if re.match(explain, word):
        return True
    return False


print(func("hello-img2.png"))
print(func("world$"))
