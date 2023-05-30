# 5. Write a Python program to generate an infinite cycle of elements from an iterable.

from itertools import cycle

for i in cycle("Hello"):
    print(i)
    if(i=='o'):break