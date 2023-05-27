# 181. write a puython program to iterate a given list cyclically at a specific index position

# way 1
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print("original:\n{}".format(l))

for i in range(3):
    l.append(l.pop(0))

print("Cycle:\n{}".format(l))


# Way 2
from collections import deque

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ld = deque(l)
print("Original:\n{}".format(list(ld)))
ld.rotate(-3)
print("Cycle:\n{}".format(list(ld)))
