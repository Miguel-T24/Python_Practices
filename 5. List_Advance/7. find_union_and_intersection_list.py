# 7. Write a python function to find union and intersection of two lists

def union_intersection(list1,list2):
    # union = set(sorted(set(list1),key=list1.index)).union(set(sorted(set(list2),key=list2.index)))
    # intersenction = set(sorted(set(list1),key=list1.index)).intersection(set(sorted(set(list2),key=list2.index)))

    union = set(list1).union(set(list2))
    intersection = set(list1).intersection(set(list2))

    return (list(union),list(intersection))

list1 = [1,2,3,4,5]
list2 =  [3,4,5,6,7,8]

union , intersection = union_intersection(list1,list2)
print("Originals: \nList1 : {}\nList2 : {}\n\nUnion : {}\nIntersection : {}".format(list1,list2,union,intersection))
