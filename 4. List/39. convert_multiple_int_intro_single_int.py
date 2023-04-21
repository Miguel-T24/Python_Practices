# 39. Write a python program to convert a list of multiple integers intro a single integer

from itertools import chain

lista = [11,33,50]

print("".join(map(str,lista)))