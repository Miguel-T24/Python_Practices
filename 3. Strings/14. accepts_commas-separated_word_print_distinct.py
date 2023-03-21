# 14. Write a python program that accepts a comma-separeted sequence of words as input and prints the distinct word in sorted form.

words = input("Enter input: ")

words = words.split(",")
words = set(words)
words = sorted(words)

print(",".join(words))