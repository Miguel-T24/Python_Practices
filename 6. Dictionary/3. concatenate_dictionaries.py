# 3. Write a python script to concatenate the following dictionaries to create a new one

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic4 = {**dic1, **dic2, **dic3}

print(dic4)


# way 2, for
d5 = {}
for d in (dic1,dic2,dic3):
    d5.update(d)

print(d5)
