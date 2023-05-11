# 41. Write a python program  to remove everything except alphanumeric character from string

from re import sub

string = '**//Python Exercises// - 12. '

result = sub("\W","",string)

print(result)