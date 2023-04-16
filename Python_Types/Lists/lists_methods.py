# Append
print("1. Append")
currencies = ["Dollar","Euro", "Pound"]
print("Original List:",currencies) # ["Dollar","Euro", "Pound"]
currencies.append("Yen")
print("Append Yen:",currencies) # ["Dollar","Euro", "Pound","Yen"]


animals = ['cat', 'dog', 'rabbit']
wild_animals = ['tiger', 'fox']
animals.append(wild_animals)
print('Updated animals list: ', animals) # ['cat', 'dog', 'rabbit', ['tiger', 'fox']]

# Extend
print("\n2. Extend")
languages1 = ['French', 'English']
languages2 = ['Spanish', 'Portuguese']
print("Original language 1:",languages1) # ['French', 'English']
print("Original language 2:",languages2) #['Spanish', 'Portuguese']

languages1.extend(languages1)
print('Languages List:', languages1) # ['French', 'English', 'Spanish', 'Portuguese']

print("Extend Tuple and sets in a list")
languages = ['French']
languages_tuple = ('Spanish', 'Portuguese')
languages_set = {'Chinese', 'Japanese'}

print("\nOriginal list:",languages) # ['French']
print("Original tuple:",languages_tuple) # ('Spanish', 'Portuguese')
print("Original set:",languages_set) # {'Chinese', 'Japanese'}

languages.extend(languages_tuple)
print('New Language List:', languages) # ['French','Spanish', 'Portuguese']
languages.extend(languages_set)
print('Newer Languages List:', languages) # ['French','Spanish', 'Portuguese','Chinese', 'Japanese']

# Insert
print("\n3. Insert: ")
vowel = ['a', 'e', 'i', 'u']
print("Original Vowel list:",vowel)
vowel.insert(3, 'o')
print('insert \'o\' in position 3 if the List:', vowel)

# Remove
print("\n4. Remove: ")

numbers = [1,2,3,4,5]
print("Original list:",numbers) # [1,2,3,4,5]
numbers.remove(3)
print("Remove 3:",numbers) #[1,2,4,5]

# Only remove one element if the element is duplicated
print("Remove only one element if element is duplicated")
numbers = [1,1,2,3,4,5]
print("Original:",numbers) #[1,1,2,3,4,5]
numbers.remove(1)
print("Duplicated element, Remove 1:",numbers) # [1,2,3,4,5]

# pop
print("\n5. Pop")
numbers = [1,2,3,4]
print("Original:",numbers) # [1,2,3,4]
x = numbers.pop()
print("Extracted Element:",x) # 4
print("List:",numbers) # [1,2,3]

print("I can extract element of whatever position")
x = numbers.pop(2)
print("Element of position 2:",x) # 3
print("list:",numbers) # [1,2]


print("\n6. Clear")
numbers = [1,2,3,4,5]
print("Original List:",numbers) # [1,2,3,4,5]
numbers.clear()
print("List Cleared:",numbers) # []

# Index
print("\n7. Index")
print("list.index[element,start,end]")
numbers = [1,2,3,4,5]
print("Original List:",numbers) # [1,2,3,4,5]
print("Search number 3: ",numbers.index(3)) # 2
# print("Search number 5 but from 0 to 3 position: ",numbers.index(5,0,3)) # Error not found

# Count
print("\n8. Count")
numbers = [1,2,3,3,3,3,4,5]
print("Original list:",numbers) # [1,2,3,3,3,3,4,5]
print("Count number 3: ", numbers.count(3)) # 4

lista = ["a",("a","b"),("a","b"),[3,4]]
print("Original:",lista)
print("count tuple (\"a\",\"b\"):",lista.count(("a","b")))
print("count [3,4]:",lista.count([3,4]))

# Sort
print("\n9. Sort")
print("list.sort(key,reverse)")
print("sorted(list,key,reverse)")

numbers = [5,3,9,1,7,6,2]
print("Original List:",numbers) # [5,3,9,1,7,6,2]
numbers.sort()
print("Sorted:",numbers) # [1,2,3,5,6,7,9]
numbers.sort(reverse=True)
print("Sorted reverse:",numbers) #[9,8,6,5,3,2,1]

print("Sorted using key")

def takeSecond(e):
    return e[1]

random = [(2, 2), (3, 4), (4, 1), (1, 3)]
print("Original List:",random) # [(2, 2), (3, 4), (4, 1), (1, 3)]

random.sort(key=takeSecond)
print("Sorted by second element of the tuple",random) # [(4,1),(2,2),(1,3),(3,4)]

# Reverse
print("\n10. Reverse: ")
numbers = [2,3,5,7]
print("Original List:",numbers) # [2,3,5,7]
numbers.reverse()
print("list reversed:",numbers) # [7,5,3,2]

print("Print OS")
systems = ["Windows", "MacOS","Linux"]
print("Original List of system:",systems) # ["Windows", "MacOS","Linux"]

for i in reversed(systems):
    print(i, end=" ")


# Shadow Copy
print("\n\n11. Shadow Copy")

old_list = [1,2,3,4]
new_list = old_list.copy()

print("Old List:",old_list) # [1,2,3,4]
print("New List",new_list) # [1,2,3,4]

print("Im gonna add new element to old list")
old_list.append(5)
print("Old List:",old_list) # [1,2,3,4,5]
print("New List",new_list) # [1,2,3,4]


print("if i copy list this way (list1 = list2) will happen the next")

list1 = [1,2,3,4,5]
list2 = list1

print("List1 :",list1)
print("List2 :",list2)

print("But if i add new element to one of the two list, happen the next")
list1.append(6)
print("List1 :",list1)
print("List2 :",list2)