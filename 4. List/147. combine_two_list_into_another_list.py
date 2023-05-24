# 147. Write a ython program to combina two lista into another list randomly

from random import randint

list1 = [1, 2, 7, 8, 3, 7]
list2 = [4, 3, 8, 9, 4, 3, 8, 9]
temp = list1+list2
result = []

for i in temp:
    result.append(temp.pop(randint(0,len(temp)-1)))

print(result+temp)
