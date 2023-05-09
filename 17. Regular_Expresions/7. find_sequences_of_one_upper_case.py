# 7. Write a python program to find sequences of lowercase letters joined by an undescore

import re

def lower_joined_underscore(string):
    return bool(re.search("^[a-z]+_[a-z]+$", string))

print(lower_joined_underscore("aab_cbbbc"))
print(lower_joined_underscore("aab_Abbbc"))
print(lower_joined_underscore("Aaab_abbbc"))