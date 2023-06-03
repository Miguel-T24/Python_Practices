# 2. Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'I'. Ensure that each character is used only once.

from itertools import permutations

v = ['a','e','i','o','u']

r = list(permutations(v))
print(len(r))
for i in r:
    print("".join(i))