# 33. Write a python program to find all five-charcater words in a string

from re import findall

string = 'The quick brown fox jumps over the lazy dog.'

result = findall("\w*\w{5}\w*",string)
print(result)