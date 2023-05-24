# 56. Write a python program to add two given lists of different lengths, starting on the right

list1 = [2, 4, 7, 0, 5, 8]
list2 = [3, 3, -1, 7]

len_max = max([len(list1),len(list2)])

if len(list1)!=len_max:
    for i in range(len_max - len(list1)):
        list1.append(0)
elif len(list2)!=len_max:
    for i in range(len_max - len(list2)):
        list2.append(0)

print("{}\n{}".format(list1[::-1],list2[::-1]))

result = list(map(lambda x,y:x+y, list1[::-1],list2[::-1]))

print(result)