# 44. Write a pthon program to generate groups of five consecutive numbers in a list

from random import randint
from itertools import islice

lista = []
for i in range(5):
    random = randint(0,100)
    lista.append(list(islice(range(100),random,random+5)))

print(lista)