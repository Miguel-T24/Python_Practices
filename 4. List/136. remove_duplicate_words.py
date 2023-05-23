# 136. Write a python program to remove a duplicate words from given list of strings

strings = ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
print(strings)
result = sorted(set(strings), key=strings.index)
print(result)