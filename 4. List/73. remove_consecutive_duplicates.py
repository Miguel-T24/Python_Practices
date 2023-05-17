# 73. Write a python program to remove consecutive (following each other continuosly) duplicates (elements) from given list

list1 = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

result = [list1[0]]

for i in range(len(list1)):
    if(i!=0):
        if(list1[i]!=list1[i-1]):
            result.append(list1[i])

print(result)