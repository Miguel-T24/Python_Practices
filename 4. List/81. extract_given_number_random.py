# 81. Write a python program to extract a goven number of randomly selected elements from a given list

from random import choices

lista = [1, 1, 2, 3, 4, 4, 5, 1]

print(choices(lista,k=3))