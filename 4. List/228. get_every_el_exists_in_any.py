# 228. Write a python program to get every element that exist in any of the two given lists once, after applying the provided function to each element of both

def union_by_el(x, y, fn):
  _x = set(map(fn, x))
  return list(set(x + [item for item in y if fn(item) not in _x])) 
from math import floor
print(union_by_el([4.1], [2.2, 4.3], floor))