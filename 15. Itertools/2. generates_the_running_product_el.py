# 2. Write a python program that generates the running product of elements in an iterable

from itertools import accumulate
from operator import mul

l = list(range(1,6))

for i in accumulate(l,mul):
    print(i)