# 11. Write a python program that matches a word at the end of a string, with optional punctuation

from re import search

def word_end(string):
    return bool(search("[\w.?]$",string))

print(word_end("Hola mundo")) # True
print(word_end("Hola mundo.")) # True
print(word_end("Hola mundo ")) # False