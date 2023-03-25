# 10. Write a python program to remove all the elements of a given deque object.

from collections import deque

dq = deque([1,2,3,4,5,6])
print("Original Deque: {}".format(dq))

dq.clear()
print(dq)

