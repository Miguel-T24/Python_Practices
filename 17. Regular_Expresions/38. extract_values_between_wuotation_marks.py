# 38. Write a python program to extract values between quotation marks of a string

from re import findall

string = '"Python", "PHP", "Java"'
result = findall("\w+",string)

print(result)