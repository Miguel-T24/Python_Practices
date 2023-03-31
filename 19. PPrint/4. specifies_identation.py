# 4. Write program that specifies the identation while printing a nested dictionary using the pprint module

from pprint import pprint, PrettyPrinter

nested_dict = {
    's1': {
        'a': 2,
        'c': 1,
        'b': 3
    },
    's2': {
        'f': 3,
        'e': 4,
        'd': 6
    },
    's3': {
        'g': 17,
        'h': 18,
        'i': 9
    },
    's4': {
        'a': 7,
        'j': 8,
        'k': 19
    }    
}

pp = PrettyPrinter(indent=4)
pp.pprint(nested_dict)
pp = PrettyPrinter(indent=15)
pp.pprint(nested_dict)