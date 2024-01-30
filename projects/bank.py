# class bank:
#
#     account_number = ""
#     account_holder = ""
#     balance = 0.0
#
#     def __init__(self, account_number, account_holder, balance):


def combinator_sentence(str1, str2):
    assert isinstance(str1, (str)), "str1 not can be number"
    assert isinstance(str2, (str)), "str2 not can be number"
    return str1 + str2


print(combinator_sentence(3, "10"))

"""
def balance_list(balance):
    poz = 0
    neg = 0
    zero = 0
    for i in balance:
        if i > 0:
            poz += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1
    if poz == neg and zero == 0:
        print(balance)
    else:
        balance.reverse()
        print(balance)


balance_list([1, 3, -4, -2])
"""
