# 40. Wrte a python program to crate a dictionary of keys x, y and z where each keys has as values list form 11-20,-21-30 and 31-40 resppectively. Access the fith value of each key form the dictionary

dic = {"x":list(range(11,20)), "y":list(range(21,30)), "z":list(range(31,40))}

print(dic)

for k,v in dic.items():
    print("{} : {}".format(k,v[4]))
