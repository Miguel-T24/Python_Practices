# 11.  Write a ptyhon program that copies a deque object and verifies shadow copying

import collections

a = collections.deque([1,2,3,4])
print("Orginal: {}".format(a))

b = a.copy()
print(a)
print(b)

b.append(5)
print(a)
print(b)