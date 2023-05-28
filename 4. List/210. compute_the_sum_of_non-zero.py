# 210. Write a python program to compute the sum of non-zero groups (separated by zeros) of given  list of numbers

l = [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1, 0, 0, 0]

temp = []
r = []

for i in range(len(l)-1):
    if(l[i]!=0):
        temp.append(l[i])
    elif(l[i]==0 and l[i+1]==0):
        pass
    if ((l[i]==0 and l[i+1]!=0) or (i==len(l)-2)):
        if(i==len(l)-2):
            temp.append(l[i+1])
        r.append(temp)
        temp = []

r = [sum(x) for x in r]
print(r)
