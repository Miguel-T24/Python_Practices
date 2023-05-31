# 0. Write a python program to split an iterable and generate iterables and specifed numbers of tiems

import itertools as it
def tee_data(iter, n):
    return it.tee(iter, n)
#List
result = tee_data(['A','B','C','D'], 5)
print("Generate iterables specified number of times:")
for i in result:
    print(list(i))