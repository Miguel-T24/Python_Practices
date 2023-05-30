# 271. Write a Python program to check if there are duplicate values in a given flat list.

l = [1, 2, 3, 4, 5, 6, 7]
print(not(len(l) == len(set(l))))
l = [1, 2, 3, 3, 4, 5, 5, 6, 7]
print(not(len(l) == len(set(l))))