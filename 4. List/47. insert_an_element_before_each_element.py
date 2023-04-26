# 47. write a python program to insert an element before each elemetn of a list

from itertools import chain

lista = [1,2,3,4,5,6,7,8,9]
lista = list(map(lambda x:[x],lista))
for i in lista:
    i.insert(0,6)
lista = list(chain(*lista))

print(lista)
