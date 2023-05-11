# 31. Write a python program to replace all occurences of a space, comma, or dot with a colon

from re import sub

string = "hola, mundo.a.a."
string = 'Python Exercises, PHP exercises.'
result = sub("[ ,.]",":" ,string)

print(result)