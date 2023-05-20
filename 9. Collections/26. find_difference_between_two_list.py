# 26. Write a python program to find the difference between two lists including duplicate elements. Use the collections module

from collections import Counter
l1 = [1,1,2,3,3,4,4,5,6,7]
l2 = [1,1,2,4,5,6]
print("Original lists:")
c1 = Counter(l1)
c2 = Counter(l2)
print("Counter l1: {}".format(c1))
print("Counter l2: {}".format(c2))

diff = c1-c2
print("Diff: {}".format(diff))
print("Values:",list(diff.values()))
print("Elements:",list(diff.elements()))