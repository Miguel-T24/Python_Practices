# 5. Write a python program to square the elements of a list using the map() function

from math import sqrt
lista = [1,2,3,4,5,6]

# using map
result = list(map(lambda x : x**2 , lista))
print(result)

# usign comprehentions list
result = [x**2 for x in lista]
print(result)