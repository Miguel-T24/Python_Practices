# 26. Write a python program to match if twi word from  a lista of words strat with the letter 'P'

from re import search

words = ["Python PHP", "Java JavaScript", "c c++"]
for i in words:
    if(search("^P\w+\sP\w+",i)):
        print(i)
