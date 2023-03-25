# 1. Write a python program to create an array of 5 integers an display th array items. Access individual elements through index.

from array import array

array_num = array('i',[1,2,3,4,5])
print(array_num)

for i in array_num:
    print(i)
print("Access first three elements individually")
print(array_num[0])
print(array_num[1])
print(array_num[2])
