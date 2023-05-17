# 72. Write a python program to invert a dictionary with unique hhashable values

students = {  'Theodore': 10,
  'Mathew': 11,
  'Roxanne': 9,}

result = dict(map(lambda x:(x[1],x[0]), students.items()))

print(result)