# 79. Write a pytyhon program to remove kkth element from given list, and print the updated list

def remove_kth(lista,pos):
    lista.pop(pos)
    return lista

lista = [1, 1, 2, 3, 4, 4, 5, 1]
print("Original:",lista)
print("After Removed:",remove_kth(lista,2))