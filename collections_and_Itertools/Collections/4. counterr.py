# counter
print("Counter")

import collections

print(collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])) # Counter({'b': 3, 'a': 2, 'c': 1})
print(collections.Counter({'a':2,'b':3,'c':1})) # Counter({'b': 3, 'a': 2, 'c': 1})
print(collections.Counter(a=2,b=3,c=1)) # Counter({'b': 3, 'a': 2, 'c': 1})


print("\nEmpty Initialize")
c = collections.Counter()
print(c) # Counter()

c.update('abcdaab')
print('Sequence: ',c) # Counter({"a":3,"b":2,"c":1,"d":1})

c.update({'a':1,'d':5})
print('Dict:',c)  # Counter({"d":6,"a":4,"b":2,"c":1})

# Access to count
print("\nAccess to count")

c = collections.Counter('abcdaab')
for letter in 'abcde':
    print("{} : {}".format(letter,c[letter]))

# a : 3
# b : 2
# c : 1
# d : 1
# e : 0

print("\nElements Method")
c = collections.Counter('extremely')
c['z'] = 0
print(c) # Counter({'e': 3, 'x': 1, 't': 1, 'r': 1, 'm': 1, 'l': 1, 'y': 1, 'z': 0})
print(list(c.elements())) #['e', 'e', 'e', 'x', 't', 'r', 'm', 'l', 'y']

# most_common()
print("\nMost Common")
sales = collections.Counter(banana = 15, tomato = 4,apple = 39, orange = 30)

print(sales) # Counter({'apple': 39, 'orange': 30, 'banana': 15, 'tomato': 4})
print(sales.most_common()) # [('apple', 39), ('orange', 30), ('banana', 15), ('tomato', 4)]
print(sales.most_common(1)) # [('apple', 39) 
print(sales.most_common(2)) # [('apple', 39), ('orange', 30)]
print(sales.most_common(None)) # [('apple', 39), ('orange', 30), ('banana', 15), ('tomato', 4)]
print(sales.most_common(20)) # [('apple', 39), ('orange', 30), ('banana', 15), ('tomato', 4)]

# Arithmetic
print("\nArithmetic")
c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabet')

print("C1:",c1) # C1: Counter({'b': 3, 'a': 2, 'c': 1})
print("C2:",c2) # C2: Counter({'a': 2, 'l': 1, 'p': 1, 'h': 1, 'b': 1, 'e': 1, 't': 1})

print("\nCombined Counts:")
print(c1 + c2) # Counter({'a': 4, 'b': 4, 'c': 1, 'l': 1, 'p': 1, 'h': 1, 'e': 1, 't': 1})

print("Substraction:")
print(c1-c2) # Counter({'b': 2, 'c': 1})

print("Intersection (taking positive Minimums):")
print(c1 & c2) # Counter({'a': 2, 'b': 1})

print("Union (takng maximums): ")
print(c1 | c2) # Counter({'b': 3, 'a': 2, 'c': 1, 'l': 1, 'p': 1, 'h': 1, 'e': 1, 't': 1})