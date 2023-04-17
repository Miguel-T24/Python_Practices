# create set
print("1. create sets")
student_id = {112,114,116,118,115}
print(student_id) #{112,114,116,118,115}
vowel_letters = {'a','e','i','o','u'}
print(vowel_letters)
mixed_set = {'hello', 101,-2,'bye',True}
print(mixed_set)

# duplicate Items in a Set
print("\n2. Duplicate Items in a set")
numbers = {2,4,6,6,2,8}
print(numbers) # {2,4,6,6,2,8}

# Add update set in python
print("\n3. Add update set in python")
numbers = {21,34,54,12}
print("Original Set: ",numbers) # {34,12,21,51}
numbers.add(38)
print("New set:",numbers) # {24,38,12,21,54}

# Update python set
print("\n4. Update python set")
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ["Apple", "Google", "Apple"]
print("Companies:",companies) # {'Ralph Lauren', 'Lacoste'}
print("Tech Companies:",tech_companies) # {"Apple", "Google","Apple"}
companies.update(tech_companies)
print("update companies: ",companies) # {"Apple","Google","Ralph lauren","Lacoste"}

# Remove Element from a set
print("\n5. Remove element from a set")
languages = {'Swift',"Java","Python"}
print("Original Languages:",languages) # {'Java', "Swift", "Python"}
languages.discard("Java")
print("Discard Java:",languages) # {'Swift', "Python"}

# Iterate Over a Set
print("\n6. Iterate over set")
fruits = {"Apple","Peach", "Mango"}
for fruit in fruits:
    print(fruit)

# Find number of Set Element
print("\n7. Find number of set element")
even_numbers = {2,4,6,8}
print("Set:",even_numbers) # {8,2,4,6}
print("Number of set: ",len(even_numbers)) # 4