# 23. Write a python program to flatten a shadow list

import itertools

lista = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]

lista = list(itertools.chain(*lista))

print(lista)