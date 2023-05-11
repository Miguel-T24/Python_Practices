# 57. Write a python program that checks whether a word starts and ends with a vowel ina  given string. 

from re import search

def start_end_vowel(string):
    return bool(search("^[aeiou]+.*[aeiou]+$", string))

print(start_end_vowel("Red Orange White"))
print(start_end_vowel("Red White Black"))
print(start_end_vowel("abcd dkise eosksu"))