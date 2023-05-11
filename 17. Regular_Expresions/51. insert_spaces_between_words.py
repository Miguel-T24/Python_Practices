# 51. Write a python program to insert spaces between words starting with capital letters

from re import sub

string = "holaMundo"

result = sub("(\w)([A-Z])",r"\1 \2", string)
print(result)