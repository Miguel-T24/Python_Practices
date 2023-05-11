# 34. Write a python program to find all three, four, and five charcater words in string

from re import findall

string = 'The quick brown fox jumps over the lazy dog.'

result = findall("\w*[\w{3,5}]\w*",string)

print(result)