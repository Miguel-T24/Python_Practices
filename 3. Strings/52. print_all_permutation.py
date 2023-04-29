# 52. Write a python program to print all permutations

from itertools import permutations

string = "xyz"

for i in permutations(string):
    print("".join(i))

print(list(permutations(string)))