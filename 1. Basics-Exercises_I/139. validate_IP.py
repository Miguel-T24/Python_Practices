# 139. Write a python program to valide an ip address

import socket
addr = '127.0.0.2561'
try:
    socket.inet_aton(addr)
    print("Valid IP")
except socket.error:
    print("Invalid IP")