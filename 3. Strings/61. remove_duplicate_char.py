# 61. Write a python porgram ot remove duplicate characters from a given string

from collections import OrderedDict
def remove_duplicate(str1):
  return "".join(OrderedDict.fromkeys(str1))
     
print(remove_duplicate("python exercises practice solution"))
print(remove_duplicate("w3resource"))