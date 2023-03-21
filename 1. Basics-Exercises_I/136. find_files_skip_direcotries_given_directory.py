# 136. Write a python program to find files and skip directories in a given direcotry

import os

print([f for f in os.listdir('/home/students') if os.path.isfile(os.path.join('/home/students', f))])