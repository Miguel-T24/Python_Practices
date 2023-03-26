# 8. Write a python program to convert an array to an array of mahcine values and return the bytes representation


from array import array
print("Bytes to String: ")
x = array('b', [119, 51, 114, 101,  115, 111, 117, 114, 99, 101])
s = x.tobytes()
print(s)