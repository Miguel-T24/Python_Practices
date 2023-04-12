# 21. Write a python program to get the array size of types unsigned integer and float

from array import array

array1 = array('i',(12,25))
print(array1.itemsize)

array2 = array('f', (12.236,36.36))
print(array2.itemsize)