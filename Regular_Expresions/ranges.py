# ranges

import re

lista_nombres = [
    'Ana',
    'Pedro',
    'Maria',
    'Rosa',
    'Sandra',
    'Celia'
]

for i in lista_nombres:
    if (re.findall('[o-y]', i)):
        print(i)

codes = [
    'Ma1',
    'Se1',
    'Ma2',
    'Ma3',
    'Val1',
    'Val2',
    'Ma4'
]

# Todos los pedidos de madrid entre el 0 y el 3
for i in codes:
    if (re.findall("Ma[1-3]", i)):
        print(i)

# Negacion del rango
print('\nNegacion:')
for i in codes:
    if (re.findall("Ma[^1-3]", i)):
        print(i)

codes = [
    'Ma.1',
    'Se1',
    'Ma2',
    'Ba1',
    'Ma:3',
    'Val1',
    'Val2',
    'Ma4',
    'MaA',
    'Ma.5',
    'MaB',
    'Ma:C'
]


print("\nElemntos que contengan . o :")
for i in codes:
    if (re.findall('Ma[.:]',i)):
        print(i)