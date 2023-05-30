# 1. Write a python program to create an iterator form a several iterables in a sequence and display the type and elements of the new iterator

from itertools import chain

l1 = list(range(1,4))
l2 = list(range(4,7))
l3 = list(range(7,10))

result = chain(l1,l2,l3)

print(type(result))
print(list(result))