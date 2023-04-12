# 11. Write a python to remove a specified item using the index of an array

from array import array
array_num = array('i',[1,2,3,4,5])

print("Original Array : {}".format(array_num))

array_num.pop(2)
print("Remove Item : {}".format(array_num))