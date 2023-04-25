# 21. Write a python program that multiplies each number in a list with a given number using lambda function

given = 3
lista = [1,2,3,4]

result = list(map(lambda x: x*given,lista))

print(result)