"""
n = True
count = 0
while n:
    result = input("please enter string: ")
    list_of_words = []
    if result == "z":
        n = False
    else:
        list_of_words.append(result)
        if result[0] == result[-1] == "x":
            count += 1
        # check = [result]
        # if check[0] == "x" and check[-1] == "x":
        #     count += 1

print(count)
"""


def check_word():
    num_of_words = 0
    num_of_unicke = 0
    num_of_repeat = 0
    file_path = input("enter the address ")
    with open(file_path, mode="r") as file:
        worders = file.read()
        print(worders)
    list_line = worders.split(" ")

    num_of_words += len(list_line)
    print(f"the number is: {num_of_words}")
    set_word = set(list_line)
    print("the number of unick is :", len(set_word))
    count = dict()
    words = worders.split(" ")
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    print(count)
check_word()
