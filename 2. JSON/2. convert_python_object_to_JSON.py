# 2. Write a python program to convert python object to JSON data

import json

python_obj = {
    "Name" : "David",
    "Class" : "I",
    "Age" : 6
}

print(type(python_obj))

j_data = json.dumps(python_obj)

print("JSON DATA:")
print(j_data)
