# 20. write a ptuyhon program to find the item with the highest frecuency in a given list


import collections

lista = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]

print(collections.Counter(lista).most_common(1)[0])