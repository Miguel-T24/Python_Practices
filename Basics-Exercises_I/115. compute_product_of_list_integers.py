# 115. Write a python program to compute the product of a list integers (without using a for loop).

from functools import reduce
lista = [10,20,30]

new_lista = reduce(lambda x,y:x*y, lista )

print(new_lista)