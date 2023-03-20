# 24. Write a python program to test whether a passed letter is a vowel or not

letter = input("Enter a letter: ")

vowel = 'aeiou'

if letter in vowel:
    print("{} is a vowel".format(letter))
else:
    print("{} is not a vowel".format(letter))