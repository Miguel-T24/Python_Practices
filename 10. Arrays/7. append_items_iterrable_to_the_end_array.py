# 7. Write a python program to append otemas from iterable to the end of the array

from array import array

array_num = array('i',[1,3,5,7,9])
print("original:",array_num)

array_num.extend(array_num)
print("Extend:",array_num)