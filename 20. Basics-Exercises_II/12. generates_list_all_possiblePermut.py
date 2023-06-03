# 12. Write a Python program that generates a list of all possible permutations from a given collection of distinct numbers.

from itertools import permutations
l = [1,2,3]
print(list(permutations(l)))
