# 223. wirte a python program to create a lists with non-unique values filtered out.

# way 1
l = [1,2,2,3,4,4,5]

print(l)
l = dict(zip(l,[None]*len(l)))
print(l)
l = list(l)
print(l)

# way 2
from collections import OrderedDict

l = [1,2,2,3,4,4,5]
l = OrderedDict.fromkeys(l)
print(l)
l = list(l)
print(l)