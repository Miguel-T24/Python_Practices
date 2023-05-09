# 14. Write a python program to match a string that contains only upper and lower case letters, numbers, and underscores

from re import search

def test(string):
    return bool(search("^[\w]*$",string))

print(test("The quick brown fox jumps over the lazy dog.")) # False
print(test("Python_Exercises_1")) # True