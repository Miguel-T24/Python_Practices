# 7. write a python function that accepts a string and counts the number of upper and lower case letters

def count_upper_lower(string):
    countu = 0
    countl = 0

    for i in string:
        if(i.islower()):
            countl += 1
        elif(i.isupper()):
            countu +=1
    return countu, countl

count_upper , count_lower = count_upper_lower("The quick Brow Fox") 

print("Number of Upper case : {}\nNumber of Lower case : {}".format(count_upper,count_lower))
