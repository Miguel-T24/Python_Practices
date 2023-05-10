# 21. Write a python program to find the substring within a string

from re import search

def find_substring(string,sub):
    return search(sub, string).group()

print(find_substring('Python exercises, PHP exercises, C# exercises', "exercises"))