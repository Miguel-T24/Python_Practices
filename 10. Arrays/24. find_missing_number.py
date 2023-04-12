# 24. Write a python program to find the misssing number in a given array of numbers between 10 and 20

from array import array

def missing(array_test):
    return  sum(list(range(10,21))) - sum(array_test)

array1 = array('i', [10,11,12,13,14,16,17,18,19,20])
print("The missing Value is {}".format(missing(array1)))

array2 = array('i', [10,11,12,13,14,15,16,17,18,19])
print("The missing Value is {}".format(missing(array2)))