# 31. Write a python program to count the frequency of consecutive duplicate elements in a given list of numbers. Use the itertools module

from itertools import groupby

l = [1,1,2,2,2,4,4,4,5,5,5,5]
l = groupby(l)


for n,freq in l:
    # print(n,list(freq))
    print("Number: {} , Frequency: {}".format(n,len(list(freq))))