# 13. Write a python program to convert an array to an ordinary list with the same items

from array import array

array = array('i',[1,2,3,4,5])

print("Original Array : {}".format(array))

array = list(array)

print("Array converted to list : {}".format(array))
