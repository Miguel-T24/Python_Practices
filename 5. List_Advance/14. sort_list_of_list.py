# 14. Write a python function to sort a list of list

from itertools import chain

def sorted_list_lists(lista):
    return sorted(list(chain(*lista)))

lista = [[1, 4, 5], [1, 3, 4], [2, 6, 7, 8]]
print(lista)
print(sorted_list_lists(lista))
print("\n")
lista = [[1, 2], [-1, -2, -3], [0]]
print(lista)
print(sorted_list_lists(lista))