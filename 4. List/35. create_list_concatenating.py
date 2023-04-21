# 35. Write a python program to create a lists by concatenating a given list with a range from 1 to n
from itertools import chain

def list_concat(lista,n):
    conc_list = []
    for j in range(len(lista)):
        if(j != 0):
            for i in range(1,n+1):
                conc_list.append([lista[j-1]+str(i), lista[j]+str(i)])
    return list(chain(*conc_list))

print(list_concat(['p','q'], 5))