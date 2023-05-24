# 143. Write a python program to get the frecuency of elements in a given list of lists

from collections import Counter
from itertools import chain

lista = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
result = Counter(chain(*lista))

print(dict(result))