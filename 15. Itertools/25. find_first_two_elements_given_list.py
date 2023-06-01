# 25. Write a python porgram to find two elements fo a given lists whose sum is equal to given value. Use the itertools module to solve the problem

from itertools import combinations, repeat

l = [1,2,3,0,4,5]

r = combinations(l,2)
r = [x for x in r if sum(x)==3]
print(list(r)[:2])