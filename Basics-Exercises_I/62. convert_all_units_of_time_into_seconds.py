# 62. Write a python program to convert all nuits of time into seconds

days = int(input("Input days: ")) * 3600 * 24
hours = int(input("Input hours: ")) * 3600
minutes = int(input("Input minutes: ")) * 60
seconds = int(input("Input seconds: ")) 

time = days + hours + minutes + seconds

print("The amounts of seconds: {}".format(time))
