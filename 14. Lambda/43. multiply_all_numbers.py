# 43. Write a python program ot multiply all the numbers in a given list using lambda

from functools import reduce

def multiply_list(lista):
    return reduce(lambda x,y :x*y, lista)

list1 = [4, 3, 2, 2, -1, 18]
list2 = [2, 4, 8, 8, 3, 2, 9]
print(multiply_list(list1))
print(multiply_list(list2))