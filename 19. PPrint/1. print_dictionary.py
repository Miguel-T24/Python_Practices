# 1. Wrote a python program to print a dictionary, nested dictionary, list of dictionaries of dictionaries using the pprint module

from pprint import pprint


netehan_dict = {'Name': 'Metehan Christel', 'Age': 22, 'City': 'London', 'Country': 'United Kingdom'}

pprint(netehan_dict)

print()


pprint(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

print("\nPrint nested dictionary:")
student = {1: {'name': 'Shauna Mathews', 'age': '12'},
           2: {'name': 'Alexandra Powell', 'age': '11'},
           3: {'name': 'Aled Carney', 'age': '11'},
           4: {'name': 'Dennis Walker', 'age': '10'},
           5: {'name': 'Leia Thomas', 'age': '12'}} 
pprint(student)

print("\nList of dictionaries of dictionaries:")
list_of_dicts = [
  {
    "dict1": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  {
    "dict2": {
      "key3": "val3",
      "key4": "val4"
    }
  }
]
pprint(list_of_dicts)