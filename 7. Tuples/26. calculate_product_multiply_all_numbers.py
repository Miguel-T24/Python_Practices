# 26. Write a python program to calculate the product, multiplying all the numnbers in a given tuple

from functools import reduce

def mul_tupl(tupl):
    return reduce(lambda x,y: x*y, tupl)

tupla1 = (4, 3, 2, 2, -1, 18)
print("Tupla1: {}".format(tupla1))
print("Product: {}".format(mul_tupl(tupla1)))

tupla2 = (2, 4, 8, 8, 3, 2, 9)
print("Tupla1: {}".format(tupla2))
print("Product: {}".format(mul_tupl(tupla2)))
