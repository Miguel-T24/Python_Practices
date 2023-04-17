# create String
string1 = 'Python Programming'
print(string1)

# Access String characters in python
greet = "Hello"
print(greet[1])
print(greet[-2])

# String are immutable
message = "Hola Amigos"
# message[0] = 'h' #Error
print(message) # Hola Amigos
# I can new string
message = "Hello Friends"
print(message) # Hello Friends

# Multiline String
message = """
Never gonna give you up
Never gonna let you down
"""

print(message)

# Comparate Two String
str1 = "Hello World"
str2 = "I love you python"
str3 = "Hello World"

print(str1 == str2)
print(str1 == str3)

# Join Two or More String
greet = "Hello "
name = "Jake"
result = greet + name
print(result)


# Iterate through a python string

greet = "Hello"
for letter in greet:
    print(letter)

# String Length
greet = "Hello"
print(len(greet))

# String Membership Test
print("a" in "program")
print("at" not in "battle")

# Escape Sequence in python

example = "He said, \"What's there\""
print(example)

# Plrint String Formatting (f-strings)
name = 'Cathy'
country = "UK"

print(f'{name} is from {country}')