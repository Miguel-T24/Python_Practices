# 27. Write a python program to separate and print the numbers in a given string

from re import split

text = "Ten 10, Twenty 20, Thirty 30"

result = split("\D+",text)

for i in result:
    print(i)