# 4. Write a puython prohgram that matches a string that has an a followed by zero or one 'b'

import re

def matches_zero_one_b(string):
    return bool(re.search("ab{0,1}", string))

print(matches_zero_one_b("ab"))
print(matches_zero_one_b("abc"))
print(matches_zero_one_b("abbc"))
print(matches_zero_one_b("aabbc"))
print(matches_zero_one_b("aac"))