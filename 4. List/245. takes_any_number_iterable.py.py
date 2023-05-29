# 245. Write a Python program that takes any number of iterable objects or objects with a length property and returns the longest one.

def longest_item(*args):
  return max(args, key = len)
print(longest_item('this', 'is', 'a', 'Green'))  
print(longest_item([1, 2, 3], [1, 2], [1, 2, 3, 4, 5])) 
print(longest_item([1, 2, 3, 4], 'Red'))

