# 3. Qrite a python program that specifies the width of the output while printing a list, dictionary using the pprint module

import pprint

colors = ["Red", "Green", "Blue", "White", "Pink"]
print("List with specific width:")
pp = pprint.PrettyPrinter(width=10)
pp.pprint(colors)
print("\nDictionary with specific width:")
nested_dict = {
    'd1': {
        'a': 2,
        'c': 1,
        'b': 3
    },
    'd2': {
        'f': 3,
        'e': 4,
        'd': 6
    },
    'd3': {
        'g': 17,
        'h': 18,
        'i': 9
    }
}
pp.pprint(nested_dict)