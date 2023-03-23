dic1 = {1:"a" , 2:"b"}
dic2 = {3:"c" , 4:"d"}

# Two Ways

# way 1:
print({**dic1,**dic2})

# way 2:
dic3 = {}
for dic in (dic1,dic2):
    dic3.update(dic)
print(dic3)