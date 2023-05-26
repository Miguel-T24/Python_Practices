# 167. Write a python program to convert a given list of string into list of lists

lista = ['Red', 'Maroon', 'Yellow', 'Olive']

result = list(map(lambda x:list(x),lista))

print(result)