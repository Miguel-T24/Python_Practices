# 2. Write a python program to add three given lists using python map and lambda

lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [7,8,9]

lista4 = list(map(lambda x , y , z : x + y + z, lista1,lista2,lista3))

print(lista4)