# 26. Write a python program to compute the summation of the absolute diffreenc eof all distinct pairs in a given array (non-decreasing order).

def abs_diff(l):
    return abs(abs(l[0]) - abs(l[-1]) + abs(l[0]) -  abs(l[1]) + abs(l[1]) - abs(l[-1]))

print(abs_diff([1,2,3]))
print(abs_diff([1,4,5]))