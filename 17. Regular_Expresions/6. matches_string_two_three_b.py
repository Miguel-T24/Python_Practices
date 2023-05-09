# 6. Write a python program that matches a string that has an a followed by two to three 'b'

import re

def a_two_to_three_b(string):
    return bool(re.search("ab{2,3}", string))

print(a_two_to_three_b("ab"))
print(a_two_to_three_b("aabbbbbc"))