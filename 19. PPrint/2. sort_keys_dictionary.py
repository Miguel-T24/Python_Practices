# 2. Writea python program to sort the keys of a dictionary before printing it using the pprint module

from pprint import pprint

colors = {
    'Red': 10,
    'Green': 20,
    'White': 30,
    'Black': 40,
    'Blue': 50,
    'Orange': 70
  }
print("Sort the keys of a dictionary before printing it:")
pprint(colors, sort_dicts=True)

