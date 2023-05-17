# 80. Write a python program to find the key of the maximum values in a dictionary

dict1 = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
max_value = max(dict1.values())

result = list(filter(lambda x:dict1[x] == max_value, dict1.keys()))

print("Max value: {}".format(max_value))
print("Keys: {}".format(result))