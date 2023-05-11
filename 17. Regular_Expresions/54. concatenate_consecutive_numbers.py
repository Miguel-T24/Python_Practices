# 54. Write a python program to concatenate the consecutive numbers in a given string

from re import sub

string = "Enter at 1 20 Kearny Street. The security desk can direct you to floor 1 6. Please have your identification ready."

print("original: {}".format(string))

result = sub("(\d+)\s+(\d+)",r"\1\2",string)

print("After: {}".format(result))
