# 42. Write a python program to calculate the product of given list of numbers using lambda

from functools import reduce

list1 =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reduce(lambda x,y:x*y,list1))

list2 = [2.2, 4.12, 6.6, 8.1, 8.3]
print(reduce(lambda x,y:x*y,list2))