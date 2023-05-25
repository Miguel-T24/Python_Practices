# 162. Write a python program to find the last occurrence of a specified item in a given list

lista = ['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
print(lista)
print(lista[::-1])

print("Last Ocurrence of 'f' is {}".format(len(lista) - (lista[::-1].index('f')) - 1))
print("Last Ocurrence of 'c' is {}".format(len(lista) - (lista[::-1].index('c')) - 1))
print("Last Ocurrence of 'k' is {}".format(len(lista) - (lista[::-1].index('k')) - 1))
print("Last Ocurrence of 'w' is {}".format(len(lista) - (lista[::-1].index('w')) - 1))
