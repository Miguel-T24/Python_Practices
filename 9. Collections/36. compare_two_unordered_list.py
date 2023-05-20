# 36. Write a python program to compare two unordered lists (not sets).

import collections

d1 = collections.OrderedDict([("A",1),("B",2),("C",3)])
d2 = collections.OrderedDict([("B",2),("C",3),("A",1)])

print(d1 == d2) # False

d1 = {("A",1),("B",2),("C",3)}
d2 = {("B",2),("C",3),("A",1)}

print(d1==d2) # True
