# 1. Write a python program to convert JSON data to python object

import json

json_obj = '{"Name" : "David" , "Class" : "I" , "Age" : 6}'
print("Json Object:",json_obj)

python_obj = json.loads(json_obj)
print("\nPython Object:",python_obj)

print("\nAccess to dictionary:")
print("Name: {}".format(python_obj['Name']))
print("Age: {}".format(python_obj['Age']))

