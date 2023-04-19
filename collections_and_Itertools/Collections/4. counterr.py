# counter
print("Counter")

import collections

print(collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))
print(collections.Counter({'a':2,'b':3,'c':1}))
print(collections.Counter(a=2,b=3,c=1))


print("\nEmpty Initialize")
c = collections.Counter()
print(c)

c.update('abcdaab')
print('Sequence: ',c)

c.update({'a':1,'d':5})
print('Dict:',c)

# Access to count
print("\nAccess to count")

c = collections.Counter('abcdaab')
for letter in 'abcde':
    print("{} : {}".format(letter,c[letter]))

print("\nElements Method")
c = collections.Counter('extremely')
c['z'] = 0
print(c)
print(list(c.elements()))

# most_common()
print("\nMost Common")
sales = collections.Counter(banana = 15, tomato = 4,apple = 39, orange = 30)

print(sales)
print(sales.most_common())
print(sales.most_common(1))
print(sales.most_common(2))
print(sales.most_common(None))
print(sales.most_common(20))

# Arithmetic
print("\nArithmetic")
c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabet')

print("C1:",c1)
print("C2:",c2)

print("\nCombined Counts:")
print(c1 + c2)

print("Substraction:")
print(c1-c2)

print("Intersection (taking positive Minimums):")
print(c1 & c2)

print("Union (takng maximums): ")
print(c1 | c2)