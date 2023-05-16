# 93. Write a ptyhon porgram to extract numbers from a given string
from re import findall
# Way 1
string = "red 12 black 45 green"
result = findall("\d+",string)
print(result)

# way 2
string = string.split(" ")
result = list(filter(lambda x:x.isdigit(),string))

print(result)