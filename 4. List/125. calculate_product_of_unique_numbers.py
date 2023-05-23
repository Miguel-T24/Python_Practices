# 125. Write a python program to calculate the produc of the unique numbers in a given list

from math import prod

lista = [10, 20, 30, 40, 20, 50, 60, 40]

print(prod(set(lista)))