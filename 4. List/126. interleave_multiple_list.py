# 126. Write a python program to interleave multiple lists of the same length

from itertools import chain

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [10, 20, 30, 40, 50, 60, 70]
list3 = [100, 200, 300, 400, 500, 600, 700]

result = list(chain(*list(map(lambda x,y,z: [x,y,z], list1,list2,list3))))

print(result)