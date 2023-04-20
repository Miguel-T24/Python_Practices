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

print("\n2. Function zip_longest: return a iterator that combina the elements y several iterators in tuple")

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

print("Stopping: ")
r1 = range(5)
r2 = range(2)
for i in map(lambda x,y:(x,y,x*y),r1,r2):
    print(i,end=" ")
print()


print("\nStartmap(): similar to map")
values = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]

for i in itertools.starmap(lambda x, y: (x, y, x * y), values):
    print('{} * {} = {}'.format(*i))