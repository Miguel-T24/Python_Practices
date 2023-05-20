# 22. Wroite a python program to insert an element at the beginning of a given ordered dictionary

import collections

dict1 = collections.OrderedDict([('color1', 'Red'), ('color2', 'Green'), ('color3', 'Blue')])

print(dict1)

dict1["color4"] = 'Orange'
dict1.move_to_end('color4', last=False)

print(dict1)