# Dictionary

# Create Dictionary
print("1. Creating a Dictiornary")
capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}
print(capital_city)

# Add elements to a python dictionary
print("\n2. Add Elements to a python Dictionary")
capital_city = {"Nepal": "Kathmandu", "England": "London"}
print("Initial Dictionary:", capital_city)
capital_city["Japan"] = "Tokyo"
print("Updated Dictionary:",capital_city)

# Change value of dictionary
print("\n3. Change value of dictionary")
student_id = {111:"Eric",112:"Kyle",113:"Butters"}
print("Initial Dictionary:",student_id)
student_id[112] = "Stan"
print("Updated Dictiornary:",student_id)

# Accessing Element from a Dictionary
print("\n4. Accessing Elements from Dictiornary")
student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print(student_id[111])
print(student_id[113])

# Removing elements from dictionary
print("\n5. Removing Elements from Dictionary")
student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print("Initial Dictionary:",student_id)
del student_id[111]
print("Updated Dictionary:",student_id)

# iterating Through a Dictionary
print("\n6. Iterating Through a Dictionary")
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])