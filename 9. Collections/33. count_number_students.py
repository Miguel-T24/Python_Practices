# 33 Write a python program to count the number of studensts in an individual class

from collections import Counter

classes = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)

students = Counter(map(lambda x:x[0],classes))
print(students)
