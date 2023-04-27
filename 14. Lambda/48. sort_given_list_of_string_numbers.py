# 48. Write a python program to sort a given list of string (numbers) numerically using lambda

lista = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
lista = sorted(lista, key = lambda x:int(x))
print(lista)