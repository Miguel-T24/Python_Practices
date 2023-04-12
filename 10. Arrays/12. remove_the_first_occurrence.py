# 12. Wirte a python program to remove the first occurence of a specified element from an array

from array import array

array = array('i',[1,2,3,4,2,3])

print("Original Array : {}".format(array))

array.remove(3)

print("Remove first Ocurrence : {} ".format(array))
