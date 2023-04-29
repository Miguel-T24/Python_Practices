# 51. Write a python program to find the first non-repeating character in a given string

def first_non_repeat(string):
    for i in string:
        if string.count(i) == 1:
            return i
    return None

print(first_non_repeat('abcdef'))
print(first_non_repeat('abcabcdef'))
print(first_non_repeat('aabbcc'))