# 47. Write a python program to split a given dictionary of lists into lists of dictionaries

dict_list = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

print("Original Dic:",dict_list)
lista = []
items = list(dict_list.items())

for i in range(len(items)):
    for j in range(len(items[i][1])):
        lista.append({items[i][0]:items[i][1][j]})

print(lista)
    