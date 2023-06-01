# 29. write a python program to interleave multiple lists  of the same length. Use the itetools moduls.

from itertools import chain

l1 = [100, 200, 300, 400, 500, 600, 700]
l2 = [10, 20, 30, 40, 50, 60, 70]
l3 = [1, 2, 3, 4, 5, 6, 7]

r = list(chain(*list(map(lambda x,y,z:[x,y,z],l1,l2,l3))))

print(r)