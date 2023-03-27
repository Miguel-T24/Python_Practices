# 10. Write a python program to print the even numbers from given list

def even_numbers(lista):
    for i in lista:
        if i%2==0:
            print(i, end=" ")

even_numbers([1,2,3,4,5,6,7,8,9])