# 28. Write a python program to find the maximum, minimum aggregation pair in a given lists of integers

from itertools import combinations

l = [1, 3, 4, 5, 4, 7, 9, 11, 10, 9]
l = list(combinations(l,2))
# print(l)
maxi,mini = max(l,key=lambda x:sum(x)), min(l,key=lambda x:sum(x))
print("Max:",maxi)
print("Min:",mini)
