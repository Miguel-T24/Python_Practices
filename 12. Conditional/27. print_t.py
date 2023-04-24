# 27. Write a python program to print the alphabet pattern 'T'

for row in range(13):
    for column in range(5):
        if(column!=2 and (row>0 and row<13)):
            print(" ",end="")
        else:
            print("*",end="")
    print()
            