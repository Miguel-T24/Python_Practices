# 35. Write a python program to find all words that are at least 4 character long in a string

from re import findall

string = 'The quick brown fox jumps over the lazy dog.'

result = findall("\w*\w{4,}\w*", string)
print(result)