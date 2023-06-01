# 44. Write a python program to extract a non-zero block from a given integer list

from itertools import groupby

l = [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]
l = groupby(l, lambda x:x==0)
r = [list(x[1]) for x in l if x[0]==False]
print(r)