# 183. Write a python program to get the unique values ina  given lists of liss

from itertools import chain

l = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
l = list(chain(*l))
result = []

# way 1
from collections import OrderedDict
lr = sorted(list(OrderedDict.fromkeys(l)))
print(lr)

# way 2
l = sorted(set(l))
print(l)