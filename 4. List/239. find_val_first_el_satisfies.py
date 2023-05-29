# 239. Write a python program to find the value of the first element in the given list that satisfies the provided testing function

def find(lst, fn):
  return next(x for x in lst if fn(x)) 
print(find([1, 2, 3, 4], lambda n: n % 2 == 1))
print(find([1, 2, 3, 4], lambda n: n % 2 == 0))
