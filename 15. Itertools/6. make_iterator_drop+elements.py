# 6. Write a Python program to make an iterator that drops elements from the iterable as soon as an element is a positive number.

from itertools import dropwhile

num = [-1,-2,-3,4,-10,2,0,5,12]
print(num)
print(list(dropwhile(lambda z:z<0,num)))