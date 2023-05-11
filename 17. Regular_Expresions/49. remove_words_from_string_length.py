# 49. Write a python program to remove words from a string of length between 1 and a given number

from re import sub

def remove_string(string):
    return sub("\\b\w{1,3}\\b","",string)

print(remove_string("The quick brown fox jumps over the lazy dog."))
