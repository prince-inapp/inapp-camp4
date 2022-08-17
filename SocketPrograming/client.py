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
    while True:
        if(opt == '1'):
            msg = client_socket.recv(1024).decode()
            print(msg)
        if(opt == '2'):
            print("Enter Name:")
            name = input()
            print("enter phone number:")
            phone_number = input()
            client_socket.send('''{
            'opt':'2',
            'name':'{}',
            'phone_number':'{}'
            }'''.format(name,phone_number).encode())
            msg = client_socket.recv(1024).decode()
        




client()