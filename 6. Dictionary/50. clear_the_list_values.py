# 50. A python dictionary contains list as value. Write a python program to clear the list values in the said dictionary

dict1 = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}

print("Original: {}".format(dict1))


for i in dict1.keys():
    dict1[i].clear()

print("Result: {}".format(dict1))