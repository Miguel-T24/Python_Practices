# 201. write a python program to check if given string contains an element that is present in a list

s = "https://www.w3resource.com/python-exercises/list/"
l = ['.com', '.edu', '.tv']

r = list(map(lambda x:x in s, l))
print(any(r))


s = "https://www.w3resource.net"
l = ['.com', '.edu', '.tv']

r = list(map(lambda x:x in s, l))
print(any(r))