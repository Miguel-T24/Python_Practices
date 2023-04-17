# create String
print("1. Create Strings")
string1 = 'Python Programming'
print(string1) # Python Programming

# Access String characters in python
print("\n2.Access String Characters")
greet = "Hello"
print(greet[1]) # e
print(greet[-2]) # l

# String are immutable
print("\n3. String are Immutable")
message = "Hola Amigos"
# message[0] = 'h' #Error
print(message) # Hola Amigos
# I can new string
message = "Hello Friends"
print(message) # Hello Friends

# Multiline String
print("\n4. Multiline String")
message = """
Never gonna give you up
Never gonna let you down
"""
print(message)
"""
Never gonna give you up
Never gonna let you down
"""

# Comparate Two String
print("\n5. Comparate Two String")
str1 = "Hello World"
str2 = "I love you python"
str3 = "Hello World"

print(str1 == str2) #False
print(str1 == str3) # True

# Join Two or More String
print("\n6. Join two or more string")
greet = "Hello "
name = "Jake"
result = greet + name
print(result) # Hello Jake


# Iterate through a python string
print("\n7. Iterate through a python string")
greet = "Hello"
for letter in greet:
    print(letter)

# String Length
print("\n8. String Length")
greet = "Hello"
print(len(greet)) # 5

# String Membership Test
print("\n9. String Member Test")
print("a" in "program") # True
print("at" not in "battle") # False

# Escape Sequence in python
print("\n10. Escape Sequence in Python")
example = "He said, \"What's there\""
print(example) # He said "what's there"

# Print String Formatting (f-strings)
print("\n11. Print String Formatting (f-strings)")
name = 'Cathy'
country = "UK"
print(f'{name} is from {country}') # Cathy is form UK