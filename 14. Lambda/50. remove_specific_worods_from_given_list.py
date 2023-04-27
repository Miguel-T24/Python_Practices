# 500. Write a python program to remove a specific words from a given list using lambda

list1 = ['orange', 'red', 'green', 'blue', 'white', 'black']
list2 = ['orange', 'black']

print(list(filter(lambda x:x not in list2 ,list1)))
