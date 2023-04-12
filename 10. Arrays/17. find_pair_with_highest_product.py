# 17. Write a python program to find a pair with the highest product from a given array of integers

from array import array

array1 = array('i',[1,2,3,4,7,0,8,4])
print("Original Array1 : {}".format(array1))
array1 = sorted(array1)
print("Highest Pair : ({},{})".format(array1[-2], array1[-1]))




