# 82. Write a python program to wrap a given string into a paragraph with a given width

import textwrap
s = input("Input a string: ")
w = int(input("Input the width of the paragraph: ").strip())
print("Result:")
print(textwrap.fill(s,w))