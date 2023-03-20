# 58. Write a python program to sum the first positive integers

def sum_integer(*args):
    suma = 0
    for i in args:
        if (i > 0):
            suma = suma + i
    return print("La suma total es {}".format(suma))
    
sum_integer(1,2,3,4,5,6,1,-50)