# 18. Write a python program to check if a dictionary is empty or not

dict1 = {}
dict2 = {"a":70}
print(len(dict1))
print(len(dict2))


if not bool(dict1):
    print("Dictionary is empty")
else:
    print("Dictionary have items")


if not bool(dict2):
    print("Dictionary is empty")
else:
    print("Dictionary have items")
