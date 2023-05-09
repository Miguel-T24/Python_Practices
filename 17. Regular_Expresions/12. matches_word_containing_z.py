# 12. Write a python program that matches a word confaining 'z'

from re import search

def test(string):
    return bool(search("\w*z\w*",string))

print(test("Habia un zorro")) # True
print(test("Python es un lenguaje")) # False