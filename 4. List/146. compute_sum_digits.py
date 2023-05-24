# 146. Write a python program to compute the sum of digits of each numebr in a given list

from itertools import chain

def compute_sum(lista):
    result = list(map(lambda x:list(str(x)),lista))
    result = chain(*result)
    result = list(map(int,result))
    return sum(result)

print(compute_sum([10,2,56]))