# 48. Write a python program to remove a specified dictionary form a given list

lista = [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]

print("Original List:",lista)

print("Remove id #FF0000 from the said list dictionary:")

result = list(filter(lambda x:list(x.items())[0][1] != "#FF0000", lista))

print(result)