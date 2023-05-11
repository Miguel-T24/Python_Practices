# 53. Wroite a python program to remove lowercase substring from a given string

from re import sub

string = "HOJKAmunditoHGKBJH"

result = sub("[a-z]+","",string)

print(result)