# 255. Write a python program to perfirm a deep flating of list

from more_itertools import collapse

l = [1, [2], [[3], [4], 5], 6]
result = list(collapse(l))
print(result)