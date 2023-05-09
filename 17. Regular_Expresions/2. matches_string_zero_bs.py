# 2. Write a pytgon program that matches a string that has an a followed by one or more b's

import re

def matches_b(string):
    return bool(re.search("a[b]*", string))

print(matches_b("ac"))
print(matches_b("abc"))
print(matches_b("a"))
print(matches_b("ab"))
print(matches_b("abb"))