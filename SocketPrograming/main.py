# Socket Programming
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.inapp.com', 80))
print(s)