# 22. write a python program to find the highest 3 values of corresponfin keis in a dictionary

dic = {"a": 5,"b" : 2 , "c": 7, "d" : 1,"e" :9}
dic_items = sorted(dic.items(),key = lambda el:el[1], reverse=True)
for i in range(3):
    print(f'key: {dic_items[i][0]} <-> value: {dic_items[i][1]}')

