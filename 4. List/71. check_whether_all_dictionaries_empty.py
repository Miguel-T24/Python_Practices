# 71/ Write a ptyhon program to check whether all dictionarues in a list are empty or not

list1 = [{},{},{}]

print("Are Empty? {}".format(not any(list1)))
list2 = [{"a":1},{},{}]
print("Are Empty? {}".format(not any(list2)))
