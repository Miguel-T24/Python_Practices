# 42. Write a python program to find URLs in a string

from re import findall

string = '<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>'

result = findall('https?://\w+.\w{2,3}', string)

print(result)