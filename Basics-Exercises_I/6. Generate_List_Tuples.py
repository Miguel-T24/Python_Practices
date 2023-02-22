# 6. Write a python program that accepts a sequence of comma-separated number from the user and generates a list and tuple of those numbers

number = input("Enter number separated by comma: ")

print("List: ", list(number.split(",")))
print("Tuple: ", tuple(number.split(",")))