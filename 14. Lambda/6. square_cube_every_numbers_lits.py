# 6. Write a python program to square an dcuibe every number oin a given list of integers using lambda

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_square = list(map(lambda x : x**2,lista))
lista_cube = list(map(lambda x : x**3,lista))

print("Original:",lista)
print("Square :",lista_square)
print("Cube :",lista_cube)