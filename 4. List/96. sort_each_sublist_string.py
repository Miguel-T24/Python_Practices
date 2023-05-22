# 96. Write a python program to sort each siublist of string in a given lists of lists

lista = [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]

result = list(map(lambda x:sorted(x,key=lambda y:y[0]),lista))

print(result)