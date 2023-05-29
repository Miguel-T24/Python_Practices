# 248. Write a Python program to get the maximum value of a list, after mapping each element to a value using a given function.

def max_by(lst, fn):
  return max(map(fn, lst))
print(max_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']))