# 4. Write a python script to check whether a given key already exist in a dictionary

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def exist(x):
    if x in d:
        print("Key is presente in the dictionary")
    else:
        print("Key is not presente in the dictionary")


exist(5)
exist(9)