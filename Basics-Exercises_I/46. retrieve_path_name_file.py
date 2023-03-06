# 46. Write a python program to retrieve the path and nam eof the file currently beign executed

import os

print("Current file name {}".format(os.path.realpath(__file__)))
