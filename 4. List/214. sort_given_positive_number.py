# 214. Write a python program to sort a given positibe number ina  descending/ascending order

def asc_des(number):
    number = list(str(number))
    return int("".join(sorted(number))), int("".join(sorted(number, reverse=True)))

n = 134543
print("Original:\n{}".format(n))
print("Ascending: {}\nDescending: {}".format(*asc_des(n)))

