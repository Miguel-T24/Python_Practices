# 8. Write a python program to find the sequences of one uppercase letter followed by lower case letters.

import re

def upper_foll_lower(string):
    return bool(re.search("[A-Z][a-z]", string))

print(upper_foll_lower("AaBbGg")) # True
print(upper_foll_lower("Python")) # True
print(upper_foll_lower("python")) # False
print(upper_foll_lower("python")) # False
print(upper_foll_lower("PYTHON")) # False
print(upper_foll_lower("aA")) # False
print(upper_foll_lower("Aa")) # True
