# 52. Write a python program to extract a ilist of values from a given list of dictionaries

def extract(dic, val):
    return list(map(lambda x:x[val], dic))

print(extract([{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}], 'Science'))