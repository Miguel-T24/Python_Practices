print("ChainMap")

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

ab = collections.ChainMap(a,b)
print(ab) # ChainMap({'a':'A', 'c':'C'},{'b':'B','c':'D'})
print(type(ab)) # <class 'collections.Chainmap'>

# individual values
print("\nIndividual Values:")
print("'a' : {}".format(ab['a'])) # A
print("'b' : {}".format(ab['b'])) # B
print("'c' : {}".format(ab['c'])) # C

print("keys Values:")
print("keys: {}".format(list(ab.keys()))) # ['b','c','a']
print("values: {}".format(list(ab.values()))) # ['B','C','A']

print()
print('a' in ab) # True
print('d' in ab) # False

# Sorting out
print("\nsorting out")
a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

ab = collections.ChainMap(a,b)

print(ab) # ChainMap({'a':'A', 'c':'C'},{'b':'B','c':'D'})

print("Print C")
print("'c' : {}".format(ab['c'])) # C
print("But if a sort chainmap")
ab.maps = list(reversed(ab.maps))
print("Now ab is: {}".format(ab)) # ChainMap({'a':'A', 'c':'C'},{'b':'B','c':'D'})
print("Print c")
print("'c' : {}".format(ab['c'])) # D

# Update Values
print("\nUpdate Values")
a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

ab = collections.ChainMap(a,b)

print("Before: {}".format(ab['c']))
a['c'] = 'E'
print("After: {}".format(ab['c'])) # E
print("a: {}".format(a)) # {'a':'A','c':'E'}

# change value with chainmap
a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

ab = collections.ChainMap(a,b)
print("\nBefore: {}".format(ab))
ab['c'] = "E"
print("After: {}".format(ab))

print("a: {}".format(a))

#If we want avoid change values of original dictionary
print("\nIf we want avoid change values of original dictionary")
print("Child")
a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

ab1 = collections.ChainMap(a,b)
ab2 = ab1.new_child()

print("ab1 : {}".format(ab1))
print("ab2 : {}".format(ab2))

ab2['c'] = 'E'

print("ab1 after: {}".format(ab1))
print("ab2 after: {}".format(ab2))

# child Part 2
print("\nChild part 2")
a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}
c = {'c':'E'}


ab1 = collections.ChainMap(a,b)
ab2 = ab1.new_child(c)

print("ab1: {}".format(ab1))
print("ab2: {}".format(ab2))