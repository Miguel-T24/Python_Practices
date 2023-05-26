# 169. Write a python program to convert a given list of stirngs and characters to a single list of characters

from itertools import chain

lista = ['red', 'white', 'a', 'b', 'black', 'f']
result = list(chain(*list(map(lambda x:list(x),lista))))


print(result)