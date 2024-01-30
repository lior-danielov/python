def paige(arr, i):
    if arr[i - 1] < arr[i] > arr[i + 1]:
        return True
    return False


def check_counter(list):
    pisga = 0
    for i in range(1, len(list) - 1):
        if paige(list, i):
            pisga += 1
    return pisga


list1 = [1, 3, 2, 4, 3, 7, 1]
print(paige(list1, i=1))
print(check_counter(list1))
