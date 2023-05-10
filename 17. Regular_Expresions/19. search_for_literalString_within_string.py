# 19. Write a python program to serach for literal strings within a string

from re import search

list1 = ['dog','fox', 'hourse']
string = 'The quick brown fox jumps over the lazy dog.'

for i in list1:
    if(search(i,string)):
        print("{} Match in string".format(i))
    else:
        print("{} NO MATCH IN STRING".format(i))