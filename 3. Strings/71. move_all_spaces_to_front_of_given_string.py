# 71. Write a ptyhon program to move all spaces to the front of given string in a single traversal

def space_to_front(string):
    len_string = len(string)
    new_string = list(filter(lambda x:x!= " ", string))

    return " "*(len_string - len(new_string)) + "".join(new_string)

string = "Python Exercises"
print("Original: {}".format(string))
print("After Moving:{}".format(space_to_front(string)))

