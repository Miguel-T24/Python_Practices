# 206. write a ptyhon program to remove addciitonal spaces from a given lisst

l = ['abc ', ' ', ' ', 'sdfds ', ' ', ' ', 'sdfds ', 'huy']
r = [x.strip() if x!= " " else "," for x in l]
print(r)

