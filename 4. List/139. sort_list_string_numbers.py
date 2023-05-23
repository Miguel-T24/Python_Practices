# 139. Write a python program to sort a given list of string (numbers)

lista = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']

result = sorted(list(map(lambda x:int(x),lista)))

print(result)