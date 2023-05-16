# 89. Write a python program to remove unwanted characters form a given string

from re import sub

def remove_unwanted_chars(string):
    return sub("[^A-Za-z\s]","",string)

print(remove_unwanted_chars("Pyth*^on Exercis^es"))
print(remove_unwanted_chars("A%^!B#*CD"))