# 48. Write a python program to convert a list to a list of diccionaties

list1 = ["Black", "Red", "Maroon", "Yellow"]
list2 = ["#000000", "#FF0000", "#800000", "#FFFF00"]

result = list(map(lambda x,y: {"color_name":x,"color_code":y},list1,list2))

print(result)