# 65. Write a python program to move all zeros figits to the end of given list of numbers

list1 = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
new_list = list(filter(lambda x:x!=0,list1))
total = len(list1) - len(new_list)

for i in range(total):
    new_list.append(0)

print("Original List:",list1)
print("New List:",new_list)