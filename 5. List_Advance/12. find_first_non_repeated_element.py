# 12. Write a python program to find the first non-repeatded element ion a list

def first_non_repeat(lista):
    for i in lista:
        if(lista.count(i)==1):
            return i
    return None


lista = [1, 2, 3, 4, 5, 6, 7, 8]
print(first_non_repeat(lista))
lista = [1, 2, 3, 1, 2, 4, 5, 6, 7, 8]
print(first_non_repeat(lista))
lista = [1, 1, 2, 3, 1, 2, 3, 8, 8]
print(first_non_repeat(lista))