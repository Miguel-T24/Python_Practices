# 3. Wriite a python program to send a request to a web page, and print the response text and content, Also get the raw socker reposnse from the server

import requests

res = requests.get('https://www.google.com/')
print("Response text of https://google.com/:")
print(res.text)

print("\n==============================================================================")
print("\nContent of the said url:")
print(res.content)

print("\n==============================================================================")
print("\nRaw data of the said url:")
r = requests.get('https://api.github.com/events', stream = True)
print(r.raw)
print(r.raw.read(15))