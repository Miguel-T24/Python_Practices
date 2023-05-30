# 268. Write a python program to get a list with n elements rmeoved from the left and right


def remove_from(l,rl,n):
    if(rl == "r"):
        return l[:len(l)-n]
    elif(rl =="l"):
        return l[0+n:]
    else:
        return l
    
print([1,2,3])
print(remove_from([1,2,3],"l",1))
print(remove_from([1,2,3],"r",1))
print(remove_from([1,2,3],"z",1))