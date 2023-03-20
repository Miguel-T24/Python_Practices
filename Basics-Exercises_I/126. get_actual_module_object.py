# 126. Write a python program to get the actual module object for given object

from inspect import getmodule
from math import sqrt

print(getmodule(sqrt))

def add(x,y):
    return x + y

print(getmodule(add))