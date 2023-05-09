# 15. Write a python program that starts each string with a specific number

from re import search

def test(string):
    return bool(search("^5", string))

print(test("5-51065")) # True
print(test("6-51065")) # False