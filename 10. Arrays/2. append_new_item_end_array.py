# 2. Write a python program to append a new item to the end of the array

from array import array

array_num = array('i',[1,2,3])
print("Original:",array_num)

array_num.append(4)
print("Append: ",array_num)

