# 15. Write a python program to find all the pairs in a list whose sum is equal to a given value

from itertools import combinations

def pairs_sum(lista,n):
    lista = list(combinations(lista,2))
    return list(filter(lambda x:sum(x)==n,lista))

print(pairs_sum([1, 2, 3, 4, 5, 6, 7, 8, 9],10))
print()
print(pairs_sum([1, 2, 3, 4, 5, 6, 7, 8, 9],35))
print()
print(pairs_sum([1, 2, 3, 4, 5, 6, 7, 8, 9],5))