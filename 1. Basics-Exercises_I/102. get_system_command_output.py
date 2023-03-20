# 102. Write a python program to get system command output

import subprocess
returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
print("dir command to list file and directory")
print(returned_text)
