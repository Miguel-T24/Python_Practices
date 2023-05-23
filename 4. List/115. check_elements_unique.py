# 115. Write a python program to check if the elements of a given lists are uniqye or not

lista = [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
print(len(lista) == len(set(lista)))

lista = [2, 4, 6, 8, 10, 12, 14]
print(len(lista) == len(set(lista)))