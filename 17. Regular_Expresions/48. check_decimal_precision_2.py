# 48. Write a python program to check a decimal with a precision of 2

from re import match

decimal = "12.56"
result = match("\d+.\d{2}$", decimal)
print("Is precition 2? ->",bool(result))


decimal = "12.5616545"
result = match("\d+.\d{2}$", decimal)
print("Is precition 2? ->",bool(result))