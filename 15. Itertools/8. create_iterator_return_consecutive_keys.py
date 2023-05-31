# 8. Write a python program to create an iterator that returns consecutive keys and groups from iterable

from itertools import groupby

str1 = 'AAAAJJJJHHHHNWWWEERRRSSSOOIIUAA'
for key,group in groupby(str1):
    print("Key:", key)
    print("group:", list(group))