# 10. Write a python program that matches a word at the beginning of a string

import re

def test(string):
    return bool(re.search("^\w+", string))

print(test("The quick brown fox jumps over the lazy dog.")) # True
print(test(" The quick brown fox jumps over the lazy dog.")) # False