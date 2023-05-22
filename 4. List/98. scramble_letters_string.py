# 98. Write a python program to scramable the letters of a string in a given list

from random import sample

lista = ['Python', 'list', 'exercises', 'practice', 'solution'] 
result = list(map(lambda x:"".join(sample(x, len(x))),lista))
print(result)