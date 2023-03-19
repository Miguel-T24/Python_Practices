# 112. Write a python program to remove the first item from a specified list

# way 1

array = [1,2,3]
array.pop(0)
print(array)

array.insert(0,1)
print(array)

# Way 2
del array[0]
print(array)
