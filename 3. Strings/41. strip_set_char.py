# 41. Write a python program to strip a set of character from a string

def strip_char(string):
    return "".join(list(filter(lambda x:x not in "aeiou", string)))

print(strip_char("Hello World"))