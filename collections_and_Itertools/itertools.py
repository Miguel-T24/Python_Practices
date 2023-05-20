# itertools

print("Itertools")

import itertools

print("1. Chain: Function divide iterators")
for i in itertools.chain([1,2,3],['a','b','c']):
    print(i,end=" ")
print()
# 1 2 3 a b c

def make_iterables_to_chain():
    yield [1,2,3]
    yield ['a','b','c']

for i in itertools.chain.from_iterable(make_iterables_to_chain()):
    print(i,end=" ")
print()
# 1 2 3 a b c

print("\n2. Function zip_longest: return a iterator that combine the elements y several iterators in tuple")

for i in zip([1,2,3],['a','b','c']):
    print(i)
# (1,'a')
# (2,'b')
# (3,'c')

r1 = range(3)
r2 = range(2)

print("Zip Stops Early")
print(list(zip(r1,r2))) # [(0,0),(1,1)]

r1 = range(3)
r2 = range(2)

print("Zip_longest Processes all of the values:")
print(list(itertools.zip_longest(r1,r2))) #[(0,0), (1,1),(2,None)]

print("\n3. islice(): return a iterator that return selected elements of the iterator of input, by index")

print("Stop at 5:")
for i in itertools.islice(range(100),5):
    print(i,end=" ")
print()
# 0 1 2 3 4

print("Start at 5 and stop at 10:")
for i in itertools.islice(range(100),5,10):
    print(i,end=" ")
print()
# 5 6 7 8 9

print("by tens to 100:")
for i in itertools.islice(range(100),0,100,10):
    print(i, end=" ")
print()
# 10 20 30 40 50 60 70 80 90

print("\n4. Function  tee(): ")
r = itertools.islice(itertools.count(),5)
i1, i2 = itertools.tee(r)
print("i1: {}".format(list(i1))) # [1 2 3 4]
print("i2: {}".format(list(i2))) # [1 2 3 4]


print("\n5. Convertions of inputs")
print("Firt, take a look map() function")

print("Doubles:")
for i in map(lambda x:x*2, range(5)):
    print(i,end=" ")
print()
# 0 2 4 6 8

print("Multiples: ")
r1 = range(5)
r2 = range(5,10)
for i in map(lambda x,y:(x,y,x*y), r1, r2):
    print("{:d} * {:d} = {:d}".format(*i))
"""
0 * 5 = 0
1 * 6 = 6
2 * 7 = 14
3 * 8 = 24
4 * 9 = 36
"""

print("Stopping: ")
r1 = range(5)
r2 = range(2)
for i in map(lambda x,y:(x,y,x*y),r1,r2):
    print(i,end=" ")
print()

"""
Stopping: 
(0, 0, 0) (1, 1, 1) 
"""

print("\nStartmap(): similar to map")
values = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]

for i in itertools.starmap(lambda x, y: (x, y, x * y), values):
    print('{} * {} = {}'.format(*i))

"""
Startmap(): similar to map
0 * 5 = 0
1 * 6 = 6
2 * 7 = 14
3 * 8 = 24
4 * 9 = 36
"""

print("\n6. Producing new values: ")

for i in zip(itertools.count(1), ['a','b','c']):
    print(i)

print("count(start,step)")

"""
(1, 'a')
(2, 'b')
(3, 'c')
count(start,step)
"""

import fractions

start = fractions.Fraction(1,3)
step = fractions.Fraction(1,3)

for i in zip(itertools.count(start,step), ['a','b','c']):
    print("{}: {}".format(*i))

"""
1/3: a
2/3: b
1: c
"""


print("Cycle")
for i in zip(range(7), itertools.cycle(['a','b','c'])):
    print(i)

"""
Cycle
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'a')
(4, 'b')
(5, 'c')
(6, 'a')
"""
print("\nRepeat: Normal")
for i in range(5):
    print("Over-and-Over")
"""
Repeat: Normal
Over-and-Over
Over-and-Over
Over-and-Over
Over-and-Over
Over-and-Over
"""
print("Repeat: function Repeat")
for i in itertools.repeat('Over-and-Over',5):
    print(i)
"""
Repeat: function Repeat
Over-and-Over
Over-and-Over
Over-and-Over
Over-and-Over
"""

print("\nCombining repeat zip and map")
for i,s in zip(itertools.count(),itertools.repeat('over-and-over',5)):
    print(i,s)
"""
Combining repeat zip and map
0 over-and-over
1 over-and-over
2 over-and-over
3 over-and-over
4 over-and-over
"""

print("using map to multiply two numbers in range 0 - 4")
for i in map(lambda x, y: (x,y, x*y), itertools.repeat(2), range(5)):
    print("{} : {} = {}".format(*i))
"""
using map to multiply two numbers in range 0 - 4
2 : 0 = 0
2 : 1 = 2
2 : 2 = 4
2 : 3 = 6
2 : 4 = 8
"""

print("\n7. Filtering")
print("dropwhile function")

def should_drop(x):
    print("Testing:",x)
    return x < 1

for i in itertools.dropwhile(should_drop,[-1,0,1,2,-2]):
    print("Yielding:",i)

"""
dropwhile function
Testing: -1
Testing: 0
Testing: 1
Yielding: 1
Yielding: 2
Yielding: -2
"""

print("\nusing Filter()")
def check_item(x):
    print("Testing:",x)
    return x<1

for i in filter(check_item, [-1,0,1,2,-2]):
    print("Yielding:",i)

"""
using Filter()Testing: -1
Yielding: -1
Testing: 0
Yielding: 0
Testing: 1
Testing: 2
Testing: -2
Yielding: -2
"""
    
print("\nFilterfalse()")
def check_item(x):
    print("Testing:",x)
    return x<1
for i in itertools.filterfalse(check_item, [-1,0,1,2-2]):
    print("Yirlding:",i)

"""
Filterfalse()
Testing: -1
Testing: 0
Testing: 1
Yirlding: 1
Testing: 0
"""

print("\nCompress()")
every_thrid = itertools.cycle([False,False,True])
data = range(1,10)

for i in itertools.compress(data,every_thrid):
    print(i,end=" ")
print()
"""
Compress()
3 6 9 
"""