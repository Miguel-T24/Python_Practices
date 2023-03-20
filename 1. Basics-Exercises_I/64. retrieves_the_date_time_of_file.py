# 64. Write a python program that retrieves the date and time of file creation and modification


import os.path,  time


print("Last Modified: {}".format(time.ctime(os.path.getmtime("38. solve.py"))))
print("Created: {}".format(time.ctime(os.path.getctime("38. solve.py"))))


