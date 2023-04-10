# 11. Write a python function that takes two list and returns True if they have at least one common member.

def common_member_list(list1,list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result

print(common_member_list([1,2,3,4,5], [5,6,7,8,9]))
