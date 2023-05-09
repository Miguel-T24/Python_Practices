# 5. Write a python program that matches a string that has an a followed by three 'b'

import re 

def a_followed_by_three_b(string):
    return bool(re.search("ab{3}", string))

print(a_followed_by_three_b("abbb"))
print(a_followed_by_three_b("abbbbbc"))
print(a_followed_by_three_b("abbc"))
print(a_followed_by_three_b("abc"))