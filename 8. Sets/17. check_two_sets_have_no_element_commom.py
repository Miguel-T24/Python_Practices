# 17. Write a python program to check if two sets hava no elemetns in common

set1 = {1,2,3}
set2 = {4,5,6}
set3 = {4,7,1}

print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))