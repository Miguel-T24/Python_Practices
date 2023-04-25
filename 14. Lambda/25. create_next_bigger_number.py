# 25. Write a python program to create the next bigger number by rearranging the digits of a given number

def next_biggest(num):
    num_new = str(num)
    num_new = "".join(map(str,num_new))
    if(len(num_new)>2):
        num_new = int("".join(num_new[0]+num_new[-1]+num_new[-2]))
    elif(len(num_new) == 2):
        num_new = int("".join(num_new[1] + num_new[0]))
    else:
        return False
    
    return (False,num_new)[num_new>num]
    
print(next_biggest(121))
print(next_biggest(112))
print(next_biggest(10))
print(next_biggest(1))