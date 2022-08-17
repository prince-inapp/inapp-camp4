from http import server
import socket

def client():
    host = socket.gethostbyname('DESKTOP-DH4N9T0')
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, 12345))
    msg = client_socket.recv(1024).decode()
    print(msg)
    #msg = client_socket.recv(1024).decode()
    #print(msg)
    opt = input("Enter your choice: ")
    client_socket.send(opt.encode())
    


client()