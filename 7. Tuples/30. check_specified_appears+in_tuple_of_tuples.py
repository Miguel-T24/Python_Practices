# 30. Write a python program to check if a specified element appears in a tuple of tuples


def check(tup, el):
    for i in tup:
        if(el in i):
            return True
    return False


tupla = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))

print("Original Tuple: {}".format(tupla))


print("Check if \'White\' Present in said tuple of tuples! : {}".format(check(tupla, 'White')))
print("Check if \'Pink\' Present in said tuple of tuples! : {}".format(check(tupla, 'Pink')))
print("Check if \'Olive\' Present in said tuple of tuples! : {}".format(check(tupla, 'Olive')))
