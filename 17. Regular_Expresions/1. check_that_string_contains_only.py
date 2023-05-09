# 1. Write a python program to check that string contains only a certain set of characters (in this case a-z, A-Z and 0-9)

import re

def only_certain_set(string):
    # if(re.search("[a-z|A-Z|0-9]", string)):
    #     return True
    # else:
    #     return False
    
    return bool(re.search("[a-z|A-Z|0-9]", string))
    
print(only_certain_set("ABCDEFabcdef123450"))
print(only_certain_set("*&%@#!}{"))