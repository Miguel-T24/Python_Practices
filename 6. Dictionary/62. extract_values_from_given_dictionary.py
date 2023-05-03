# 62. Write a python programt to extract values from a given dictionary and cra5te a list of list from those values

list_of_dicts = [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 
'Zachary Simon', 'class': 'VII'}]

result = list(map(lambda x:list(x.values()),list_of_dicts))

print(result)