# 47. Write a python program to split a string with multiple delimiters

from re import split

string = 'The quick brown\nfox jumps*over the lazy dog.'

result = split("; |, |\*|,\n", string)

print(result)