# 227. Write a python program to get symmetric difference between two lists, after applying the provided function to each lists of both

def symmetric_difference_by(a, b, fn):
  (_a, _b) = (set(map(fn, a)), set(map(fn, b)))
  return [item for item in a if fn(item) not in _b] + [item
          for item in b if fn(item) not in _a]
from math import floor
print(symmetric_difference_by([2.1, 1.2], [2.3, 3.4], floor))