# 90. Write a python program to rmeove duplicate words from a given string

string = "Python Exercises Practice Solution Exercises"
string = string.split(" ")

result = " ".join(list(sorted(set(string), key=string.index)))
print("Original: {}".format(" ".join(string)))
print("Result: {}".format(result))
