# 7. Write a python program that accepts a filename from the user and prints the extension of the file

file = input("Enter filename: ")

print("The extension is: {}".format(file.split('.')[-1]))