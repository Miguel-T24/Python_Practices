# 51. A pyton dictionayr contians list as a bvalue. Write a python program to update the list values in the said dictionary

dict1 = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}

print("Original Dict: {}".format(dict1))


dict1["Math"] = [89,90,91]
dict1["Physics"] = [90,92,87]

print("Update Dict: {}".format(dict1))