# 100. Write a python program to extract common index elements from more than one given list

list1 = [1, 1, 3, 4, 5, 6, 7]
list2 = [0, 1, 2, 3, 4, 5, 7]
list3 = [0, 1, 2, 3, 4, 5, 7]

result = []
for x,y,z in zip(list1,list2,list3):
    if(x==y==z):
        result.append(x)

print(result)