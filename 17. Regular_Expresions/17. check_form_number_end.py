# 17. Write a python program to check for a unumber at the end of a string

from re import search

def test(string):
    return bool(search("\d$",string))

print(test('abcdef')) # False
print(test('abcdef6')) # True