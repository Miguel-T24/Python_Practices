# 16. Write a python program to convert a given list of string into a lists of lists usgin the map function.

lista = ["hola", "mundo"]

lista = list(map(lambda x:list(x), lista))

print(lista)