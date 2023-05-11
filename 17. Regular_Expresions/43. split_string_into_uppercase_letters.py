# 43. Write a python program to split a string into a uppercase letters

from re import findall

string ="PythonTutorialAndExercises"

result = findall("[A-Z][^A-Z]*",string)

print(result)
print(" ".join(result))