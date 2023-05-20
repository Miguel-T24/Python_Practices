# 18. Write a python program to merge more than one dictionary into a single expression

import itertools

dict1 = {'R': 'Red', 'B': 'Black', 'P': 'Pink'}
dict2 = {'G': 'Green', 'W': 'White'}

def merge_dicts(*dicts):
    print(dicts)
    result = list(map(lambda x:[list(x.items())[0] , list(x.items())[1]],dicts))
    print(result)
    result = dict(itertools.chain(*result))
    print(result)

merge_dicts({"A":1,"B":2}, {"C":3, "D":4})