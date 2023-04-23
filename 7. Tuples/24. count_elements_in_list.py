# 24. Write a python program to count the elements in a lists until an element is a tuple

num = [10,20,30,(10,20),40]

for i in range(len(num)):
    if (type(num[i]) is tuple):
        print("Count: {}".format(i))
        break