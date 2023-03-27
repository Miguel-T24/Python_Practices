# 2. Write a python function to sum all the numbes in a list

def sum_list(lista):
    suma = 0;
    for i in lista:
        suma+=i
    return suma

print(sum_list([8,2,3,0,7]))