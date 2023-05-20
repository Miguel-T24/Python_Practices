# 29. Write a python program to get the frecuency of elements in a given lists of listsuse collections module

from collections import Counter
from itertools import chain

l = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]

l = chain(*l)
print(Counter(l))