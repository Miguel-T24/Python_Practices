# 146. Write a python program to find the location fo python module sources

import imp
print("Location of Python os module sources:")
print(imp.find_module('os'))
print("\nLocation of Python sys module sources:")
print(imp.find_module('datetime'))