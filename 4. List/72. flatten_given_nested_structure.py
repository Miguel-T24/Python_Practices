# 72. Write a python program to flatten a given nested list structure.

from itertools import chain

list1 = [0, 10, 20, 30, 40, 50, [60, 70, 80], [90, 100, 110, 120]]
print("Original: {}".format(list1))
result = []
for i in list1:
    if(isinstance(i,list)):
        for j in range(len(i)):
            result.append(i[j])
    else:
        result.append(i)

print(result)
