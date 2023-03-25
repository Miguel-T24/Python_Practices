# 9. Write a python program to add more elements to a deque object from an iterable object.
from collections import deque

dq = deque([3,4,5])
print(dq)

# add end
lista_f = [6,7,8]
dq = dq + deque(lista_f)
print(dq)

# add begin
lista_i = [0,1,2]
dq = deque(lista_i) + dq
print(dq)



more_extend = 9,10,11
dq.extend(more_extend)
print(dq)

more_extend = -1,-2,-3
dq.extendleft(more_extend)
print(dq)