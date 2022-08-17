from http import server
import socket

def client():
    host = socket.gethostname()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, 12345))
    msg = client_socket.recv(1024).decode()
    print(msg)
    while msg.lower().strip() != 'exit':
        data = client_socket.recv(1024).decode()
        #print("Msg from Server:\n ", data)
        if(data.split()[0] == 'MENU'):
            print(data)
            msg = input("Enter your choice: ")
            client_socket.send(msg.encode())
    client_socket.close()
client()