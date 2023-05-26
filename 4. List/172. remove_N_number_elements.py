# 172. Write a python program to remove N number of elements from a given lists

def remove_el_list(lista,n):
    return lista[:len(lista)-n]

lista = [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
print(remove_el_list(lista,3))
print(remove_el_list(lista,5))
print(remove_el_list(lista,1))