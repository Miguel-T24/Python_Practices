# 11. Write a python program to generate combinations of a given length of a given iterable

from  itertools import combinations

# Lists
iterable = [1,2,3,4,5]
result = combinations(iterable,2)
for i,j in result:
    print(i,j)

print("*"*20)
# strings
iterable = "Python"
result = combinations(iterable,2)
for i,j in result:
    print(i,j)

print("*"*20)
