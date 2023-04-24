# 27. Write a python program to print the alphabet pattern 'U'

for row in range(7):
    for column in range(5):
        if(((row==6 and column==0) or (row==6 and column==4)) or ((row>=0 and row<6) and (column>0 and column<4))):
            print(" ",end="")
        else:
            print("*",end="")
    print()
