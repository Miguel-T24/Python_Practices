# 113. Write a python program to remove a duplicate dictionary entrie from a given list

dic = [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
print("Original:\n{}".format(dic))

dic = list(map(lambda x:(tuple(x.items())[0][0], tuple(x.items())[0][1]),dic))
print(dic)
dic = sorted(set(dic),key = dic.index)
print(dic)
dic = list(map(lambda x:dict([x]),dic))
print(dic)