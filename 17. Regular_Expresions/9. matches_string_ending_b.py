# 9. Write a python program that matches a string that has an 'a' followed by anything ending in 'b'

import re

def test(string):
    return bool(re.search("a.*b$", string))


print(test("aabbbbd")) # False
print(test("aabAbbc")) # False
print(test("accddbbjjjb")) # True