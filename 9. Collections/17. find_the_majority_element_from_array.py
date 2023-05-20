# 17. Write a python program to find the majority element from a given array of size n using the collections modules.

import collections

array = [10,10,20,30,40,10,20,10]

print(collections.Counter(array).most_common()[0][0])