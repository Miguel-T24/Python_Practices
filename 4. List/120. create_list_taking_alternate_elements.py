# 120. Write a python program to create a list taking alternate elements form a given list

lista  = ['red', 'black', 'white', 'green', 'orange']

result = list(map(lambda x:lista[x], list(range(0,len(lista),2))))

print(result)