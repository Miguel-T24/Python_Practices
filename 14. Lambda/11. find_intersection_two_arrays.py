# 11. Write a python program to find the intersection of two given arrays using lambda function


array1 = [1,2,3,5,7,8,9,10]
array2 = [1,2,4,8,9]

inter = list(filter(lambda x : x in array1, array2))

print("Originals: ")
print(array1)
print(array2)
print(inter)