#  240. Write a Python program to find the value of the last element in the given list that satisfies the provided testing function

def find_last(lst, fn):
  return next(x for x in lst[::-1] if fn(x))

print(find_last([1, 2, 3, 4], lambda n: n % 2 == 1))
print(find_last([1, 2, 3, 4], lambda n: n % 2 == 0))