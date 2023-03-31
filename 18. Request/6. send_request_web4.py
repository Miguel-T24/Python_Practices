# 6. Write a pythio program to send a requets to a web page and stop waiting for response after a given number of seconds. If a request tiems out, raise a timeout exception


import requests

print("timeout = 0.001")

try:
    r = requests.get('https://github.com/', timeout = 0.001)
    print(r.text)
except requests.exceptions.RequestException as e:
    print(e)    

print("\ntimeout = 1.0")    
try:
    r = requests.get('https://github.com/', timeout = 1.0)
    print("Connected....!")
except requests.exceptions.RequestException as e:
    print(e)