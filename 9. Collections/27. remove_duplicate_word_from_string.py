# 27. Write a python program to remove duplicate words from a given string. Use the collections module

import collections

string = "Python Exercises Practice Solution Exercises"
string = string.split()

# Using set
set_way = " ".join(sorted(set(string), key=string.index))
print(set_way)

# Using Collections module
result = ' '.join(collections.OrderedDict((w,w) for w in string).keys())
print(result)