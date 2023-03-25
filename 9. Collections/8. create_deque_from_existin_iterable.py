# 8. create deque from existing iterable object

from collections import deque

lista = [1,2,3]
tupla = 1,2,3
dictionary = {} 

lista_dq = deque(lista)
tupla_dq = deque(tupla)

print(lista_dq)
print(tupla_dq)