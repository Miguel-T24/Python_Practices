# 155. Write a python program to add two given lists of a diffreenct lengths, starting on the left

list1 = [2, 4, 7, 0, 5, 8]
list2 = [3, 3, -1, 7]

len_max = max([len(list1),len(list2)])
print(len_max)

if len(list1)!=len_max:
    for i in range(len_max - len(list1)):
        list1.append(0)
elif len(list2)!=len_max:
    for i in range(len_max - len(list2)):
        list2.append(0)

print(list1)
print(list2)
print(len(list1)==len(list2))

result = list(map(lambda x,y:x+y, list1,list2))

print(result)
