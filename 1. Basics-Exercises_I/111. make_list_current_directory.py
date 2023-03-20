# 111. Write a python program to make file from the current directory using a wildcard

import glob
file_list = glob.glob('*.*')
print(file_list)
#Specific files
print(glob.glob('*.py'))
print(glob.glob('./[0-9].*'))