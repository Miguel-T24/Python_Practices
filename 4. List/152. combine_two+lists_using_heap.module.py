# 152. Wrte a python program to combine two sorted lists using the heapq module

from heapq import merge

list1 = [1, 3, 5, 7, 9, 11]
list2 = [0, 2, 4, 6, 8, 10]

print(list(merge(list1,list2)))