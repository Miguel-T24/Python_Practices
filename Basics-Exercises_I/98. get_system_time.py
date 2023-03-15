# 98. Write a python program to get system time

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time : ",current_time)