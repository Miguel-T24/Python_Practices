# 73. Write a python program to convert a list of dictionaries into a list of values corresponding to the specified key


list_dict = [{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]

result = list(map(lambda x:x['age'],list_dict))

print(result)