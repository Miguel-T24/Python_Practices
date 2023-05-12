# Deque
print("Deque")

import collections

d = collections.deque('abcdefg')
print("Deque: {}".format(d)) # ['a','b','c','d','e','f','g']
print("Length: {}".format(len(d))) # 7
print("left end: {}".format(d[0])) # a
print("right end: {}".format(d[-1])) # g

d.remove('c')
print("\nDeque remove(c): {}".format(d)) # deque(['a','b','d','e','f','g'])

print("\nExtend and append")
# Add to right
d1 = collections.deque()
d1.extend('abcdefg')
print("Extend: {}".format(d1)) 
d1.append("h")
print("Append: {}".format(d1))

# Add to left
d2 = collections.deque()
d2.extendleft(range(6))
print("Extend left: {}".format(d2))
d2.appendleft(6)
print("append left: {}".format(d2))

print("\nPop para eliminar el extremo derecho y popleft el extremo izquierdo")
d3 = collections.deque()
d3.extend(range(6))
print("Original: {}".format(d3))
d3.pop()
print("pop: {}".format(d3))
d3.popleft()
print("popleft: {}".format(d3))

# rotation
print("\nRotation:")
d4 = collections.deque(range(10))
print("Original: {}".format(d4))
d4.rotate(2)
print("right Rotation: {}".format(d4))
d4.rotate(-2)
print("left Rotation: {}".format(d4))

# Maximun
print("Maximum")
d1 = collections.deque(maxlen=5)
d1.extend(range(50))
print("d1: {}".format(d1))