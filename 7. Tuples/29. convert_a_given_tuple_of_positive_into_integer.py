# 29. Write a python program to convert a given tuple of positive integers into an integer

def convert_tuple_integer(tup):
    result = ""
    for i in tup:
        result += str(i)
    return int(result)



tupla1 = 1,2,3
print("tupla 1: {}".format(tupla1))
print("Result: {}".format(convert_tuple_integer(tupla1)))

tupla2 = (10, 20, 40, 5, 70)
print("tupla 1: {}".format(tupla2))
print("Result: {}".format(convert_tuple_integer(tupla2)))