# 58. Write a python program to replace the last element in a list with another list

from itertools import chain

list1 =  [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]

list1 = [list1[0:-1],list2]
print(list1)
print(list(chain(*list1)))

# Way 2
list1 =  [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]

list1[-1:] = list2
print(list1)