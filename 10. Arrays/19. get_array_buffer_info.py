# 19. Write a python program to get array buffer information

from array import array
a = array("I", (12,25))
print("Array buffer start address in memory and number of elements.")
print(a.buffer_info())