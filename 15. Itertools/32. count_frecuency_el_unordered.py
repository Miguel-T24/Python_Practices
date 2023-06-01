# 32. Write a python program to count the frequency of the elemnts of a given unordered list

from itertools import groupby

l = [2, 1, 3, 8, 5, 1, 4, 2, 3, 4, 0, 8, 2, 0, 8, 4, 2, 3, 4, 2]

l.sort()
print(l)
l = groupby(l)
# r = [len(list(freq)) for n,freq in l]
# print(r)

for n,f in l:
    print("Number: {}, Frequency: {}".format(n,len(list(f))))
    