# 10. Wrote a python program to insert a newly created item before the second element in an existing array

from array import array

array_num = array('i',[1,3,5,7,9])
print("Original: {}".format(array_num))

array_num.insert(1,4)
print("inserted: {}".format(array_num))

