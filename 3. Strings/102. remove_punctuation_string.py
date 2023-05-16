# 102. Write a python program to remove punctuation from a given string

from re import sub

string = "String! With. ñññPunctuation?"

result = sub("[^A-Za-z\s]","",string)

print(result)