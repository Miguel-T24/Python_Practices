# 4. Write a python program to sort a list of dictionaries using lambda 

lista = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

lista_sorted = sorted(lista, key = lambda x:x['color'])

print(lista_sorted)