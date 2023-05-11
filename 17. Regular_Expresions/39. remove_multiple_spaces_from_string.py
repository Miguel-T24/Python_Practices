# 39. Write a python program to remove multilpe spaces from a string

from re import sub

string = "Python     Exercises"

result = sub("\s+"," ", string)

print(result)