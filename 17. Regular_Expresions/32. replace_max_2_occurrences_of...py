# 32. Write a python program to replace maximum 2 occurrences of space, comma, or dot, with a colon.

from re import sub

string = 'Python Exercises, PHP exercises.'

result = sub("[\s,.]",":",string,2)
print(result)