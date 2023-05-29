# 247. Write a Python program to calculate the difference between two iterables, without filtering duplicate values.

def difference(x, y):
  _y = set(y)
  return [item for item in x if item not in _y]
print(difference([1, 2, 3], [1, 2, 4]))