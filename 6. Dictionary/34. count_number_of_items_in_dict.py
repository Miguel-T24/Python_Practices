# 34. Write a python program to count the number of items in a dictionary value that is a list

dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}

result = sum(map(len,dict1.values()))

print(result)
