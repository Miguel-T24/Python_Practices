# 134. Write a python program to find the difference bwteen two lists including dulpicate elements

list1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
list2 = [1, 1, 2, 4, 5, 6]
result = []


for i in list1:
    if(i in list2):
        list2.remove(i)
    else:
        result.append(i)



print(result)