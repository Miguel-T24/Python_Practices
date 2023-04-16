# create Lists
numbers = [1,2,5]
print("1. Creating list",numbers) # [1,2,5]

# Empty List
my_list = []
print("\n2. Empty List :",my_list) # []

# Access Python lists Elements
print("\n3. Access Python lists Elements")
languages = ['Python', "Swift", "C++"]
print(languages[0]) #Python
print(languages[2]) # C++

# Negative indexing in python
print("\n4. Negative indexing in python")
languages = ['Python', "Swift", "C++"]
print(languages[-1]) # C++
print(languages[-3]) # Python


# Slicing of a python lists
print("\n5. Slicing of a python lists")
my_list = ['p','r','o','g','r','a','m','i','z']
print(my_list[2:5])
print(my_list[5:])
print(my_list[:])

# Add Elements in a list
print("\n6. Add Elements in a list")
my_list = []
print("Empty List:",my_list) #[]
my_list.append(1)
print("Add Element in the end:",my_list) # [1]
my_list.append(2)
print("Add other Element in the end:",my_list) # [1,2]

my_list.insert(0,0)
print("Add Element in the start: ",my_list) #[0,1,2]
print("'Insert' can use to enter a value at any other position")


# Extend list
print("\n7. Extend List")
list1 = [1,2,3]
list2 = [4,5,6]

print("List 1:",list1) # [1,2,3]
print("List 2:",list2) # [4,5,6]

list1.extend(list2)
print("Extend list:",list1) #[1,2,3,4,5,6]

# Change items
print("\n8. Change Items")
languages = ['Python', 'Swift', 'C++']
print("Original:",languages) # ["Python" , "Swift" , "C++"]
languages[2] = "C"
print("Change the index 2",languages) # ["Python" , "Swift" , "C"]

# Remove item form a list
print("\n9. Remove Item from the list")
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
print("Original list:",languages) # ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
del languages[-3]
print("Remove -3 (JAVA) index:", languages) # ['Python', 'Swift', 'C++', 'C', 'Rust', 'R']

del languages[0:2]
print("Remove from 0 and 2 position index (Python and Swift)",languages) # ['C++', 'C', 'Rust', 'R']

print("Removing Specific value:")
languages.remove("C++")
print("Removing C++",languages) # ['C', 'Rust', 'R']


# Itering throught a list
print("\n10. Itering Through a list")
languages = ['Python', 'Swift', 'C++']
for i in languages:
    print(i)

# Check if value exist in the python list
print("\n11. Check if Value exist in a python list")
languages = ['Python', 'Swift', 'C++']
print("C" in languages) # False
print("Python" in languages) # True

# List Length
print("\n12. List length")
languages = ['Python', 'Swift', 'C++']
print(len(languages)) # 3

# Python List Comprehensions
print("\n13. Python Lists Comprehensions")
numbers = [number for number in range(1,6)]
print(numbers) # [1,2,3,4,5]
numbers = [number * number for number in range(1,6)]
print(numbers) # [1,4,9,16,25]