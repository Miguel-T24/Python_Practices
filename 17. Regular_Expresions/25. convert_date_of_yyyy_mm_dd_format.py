# 25. Write a python program to convertv a date of yyyy-mm-dd format to dd-mm-yyyy

from re import sub

date = "2023/05/10"
print("Original: {}".format(date))

# way 1
date = date[-2:]+ date[4:8] + date[0:4]
print("way 1: {}".format(date))


date = "2023/05/10"
# way 2
date = sub("(\d{4})/(\d{2})/(\d{2})", "\\3/\\2/\\1", date)
print("Way 2: {}".format(date))