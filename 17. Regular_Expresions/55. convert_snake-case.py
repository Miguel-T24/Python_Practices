# 55. Write a python program to convert a given string to snake case

from re import sub

string = "java-script"
result = sub("(.)[\W_](.)",r"\1_\2", string)
print(result)