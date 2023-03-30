# 6. Write a python program to convert all the characters into uppercase and lowercase and eliminate duplicate letters from a given sequence. Use the map function

def change_cases(s):
  return str(s).upper(), str(s).lower()
 
chrars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
print("Original Characters:\n",chrars)
 
result = map(change_cases, chrars)
print("\nAfter converting above characters in upper and lower cases\nand eliminating duplicate letters:")
print(set(result))
