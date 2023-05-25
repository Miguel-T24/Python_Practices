# 154. Write a python program to get items from a given list with specific conditions

lista = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]

print("Greater than 45: {}".format(lista.index(next(filter(lambda x:x>45 and x%2 == 0,lista)))))

