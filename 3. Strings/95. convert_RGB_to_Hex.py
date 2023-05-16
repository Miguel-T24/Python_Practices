# 95. Write a python program to convert the values of rgb components to hexadecimal color code

def rgb_to_hex(r, g, b):
  return ('{:02X}' * 3).format(r, g, b)
 
print(rgb_to_hex(255, 165, 1))
print(rgb_to_hex(255, 255, 255))
print(rgb_to_hex(0, 0, 0))
print(rgb_to_hex(0, 0, 128))
print(rgb_to_hex(192, 192, 192))