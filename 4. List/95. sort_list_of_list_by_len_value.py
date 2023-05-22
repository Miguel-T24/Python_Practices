# 95. Write a Python program to sort a given list of lists by length and value.

lista = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]

lista.sort()
lista.sort(key=len)
print(lista)