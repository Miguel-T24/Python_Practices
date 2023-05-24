# 148. Wrte a python program to remove specific words from a given list

lista = ['red', 'green', 'blue', 'white', 'black', 'orange']
remove = ['white', 'orange']

print("Original: \n{}".format(lista))
result = list(filter(lambda x:x not in remove,lista))
print("Result:\n{}".format(result))
