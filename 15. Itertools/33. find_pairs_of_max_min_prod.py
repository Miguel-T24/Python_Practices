# 33. Write a python program to find pairs of maximum and minimun products form  given list. Use the itertools module 

from itertools import combinations
l = [2, 5, 8, 7, 4, 3, 1, 9, 10, 1]
l = list(combinations(l,2))
print(l)

maxi,mini = max(l,key = lambda x:x[0]*x[1]),min(l,key = lambda x:x[0]*x[1])
print("Max: {}\nMin: {}".format(maxi,mini))

