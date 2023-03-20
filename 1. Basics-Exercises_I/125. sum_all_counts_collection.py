# 125. Write a python program to sum all counts in a collection

import collections

lista = [2,2,4,6,6,8,6,10,4]

result = sum(collections.Counter(lista).values())

print(result)
print(len(lista))