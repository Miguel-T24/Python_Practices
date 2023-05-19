# OrderedDict

print("Ordered Dict")

import collections

print("Regular Dictionary")
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'

print(d) # {'a': 'A', 'b': 'B', 'c': 'C'}
for k,v in d.items():
    print("{} : {}".format(k,v))
# a : A
# b : B
# c : C
    
print("\nOrdered Dict")
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'

print(d) # OrderedDict([('a', 'A'), ('b', 'B'), ('c', 'C')])
for k,v in d.items():
    print("{} : {}".format(k,v))
# a : A
# b : B
# c : C

print("\nCompare Ordered Dict")

import collections

print("\nCompare Ordered Dict")

print('Normal dict:', end=' ')
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = {}
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

print(d1 == d2) # True
print(d1) # {'a': 'A', 'b': 'B', 'c': 'C'}
print(d2) # {'c': 'C', 'b': 'B', 'a': 'A'}

print('\nOrderedDict:', end=' ')

d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = collections.OrderedDict()
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

print(d1 == d2) # False
print(d1) # OrderedDict([('a', 'A'), ('b', 'B'), ('c', 'C')])
print(d2) # OrderedDict([('c', 'C'), ('b', 'B'), ('a', 'A')])
print("False because the order is important")

print("\nReorder")

d = collections.OrderedDict(
    [('a', 'A'), ('b', 'B'), ('c', 'C')]
)

print('Before:')
for k, v in d.items():
    print(k, v)
"""
Before:
a A
b B
c C
"""

d.move_to_end('b')

print('\nmove_to_end():')
for k, v in d.items():
    print(k, v)
"""
move_to_end():
a A
c C
b B
"""

d.move_to_end('b', last=False)

print('\nmove_to_end(last=False):')
for k, v in d.items():
    print(k, v)
"""
b B
a A
c C
"""

print("\npop()")
d.pop('c')
for k,v in d.items():
    print("{}: {}".format(k,v))
"""
pop()
a: A
b: B
"""
