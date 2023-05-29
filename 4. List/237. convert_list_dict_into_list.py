# 237. Write a python program to convert a given list of dictionaries into a list of values correponding to the specified key

def pluck(l_dic,key):
    return [l_dic[i][key] for i in range(len(l_dic))]

simpsons = [
  { 'name': 'Areeba', 'age': 8 },
  { 'name': 'Zachariah', 'age': 36 },
  { 'name': 'Caspar', 'age': 34 },
  { 'name': 'Presley', 'age': 10 }
]

print(pluck(simpsons,'age'))