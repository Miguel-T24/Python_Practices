# 20. Write a python program to search for a literal string and also find the locations within the original string where the pattern occurs.

from re import search

string = "The quick brown fox jumps over the lazy dog."
find = "fox"

result = search(find, string)

print(result.span()) # (16,19)
print(result.span()[0]) # 16
print(result.span()[1]) # 19

print(result.start()) # 16
print(result.end())   # 19