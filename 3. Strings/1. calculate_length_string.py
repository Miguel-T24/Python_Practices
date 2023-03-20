# 1. Write a python program to calculate the length of string

string = "Hola Mundo"

print(len(string))


def calculate(string):
    count = 0
    for i in string:
        count +=1
    return count

print(calculate(string))
