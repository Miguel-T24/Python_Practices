# 9. Write a python rogram to append items to a specific list

from array import array

lista1 =  [1,2,3]
array_num = array('i',[])

print("List:", lista1)
print("Array:", array_num)

array_num.fromlist(lista1)

print("array: ",array_num)