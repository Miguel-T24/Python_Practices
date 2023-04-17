# All values equivalent True o empty
print("1. All")
l = [1,3,4,5]
print(all(l)) # True

l = [0,False]
print(all(l)) # False

l = [1,3,4,0]
print(all(l)) # False

l = [0,False , 5]
print(all(l)) # False

l = []
print(all(l)) # True

# Any, at least one is equivalent True
print("\n2. Any")
boolean_list = ['True', 'False', 'True']
result = any(boolean_list)
print(result) # True

# Enumarate
print("\n3. Enumarte")
languages = ['Python', "Java","Javascript"]
print(languages)
for n,i in enumerate(languages,1):
    print(n,i)

# len
print("\n4. len")
set1 = {1,2,3,4}
print(len(set1)) # 4

# Max
print("\n5. Max")
set1 = {5,2,50,-40}
print(max(set1)) # 50

# Min
print("\n6. Min")
set1 = {5,2,50,-40}
print(min(set1)) # -40

# sorted
print("\n7. Sorted")
vowel_set = {'e', 'a', 'u', 'o', 'i'}
print(vowel_set) # {'i','u','o','a','e'}
print(sorted(vowel_set , reverse=False)) # ['a','e','i','o','u']
print(sorted(vowel_set , reverse=True)) # ['u','o','i','e','a']

# sum
print("\n8. Sum")
numbers = {5,3,6,2,7}
print(sum(numbers)) # 23