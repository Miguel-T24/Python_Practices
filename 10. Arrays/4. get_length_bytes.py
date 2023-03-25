# 4. Write a ptyhon program to get the length in bytes of one arrat items in the internal representation

from array import array

array_num = array('i',[1,2,3,4,5])
print("original:",array_num)
print("Length in bytes representation", array_num.itemsize)

