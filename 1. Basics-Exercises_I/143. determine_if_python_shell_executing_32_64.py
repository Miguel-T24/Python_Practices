# 143. Write a python programm to determine if the python shell is executin in 32 or 64 bits mode on the operating system

import struct 

print(struct.calcsize("P") * 8)