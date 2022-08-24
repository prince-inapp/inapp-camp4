import json
import socket

def displayOptions():
    print('''
    1. Display All Contacts
    2. Add New Contact
    3. Delete Contact
    4. Search Contact by Name
    5. Search Contact by Number
    6. Exit
    ''')

def client():
    host = socket.gethostname() 
    port = 5000 
    client_socket = socket.socket()
    client_socket.connect((host,port)) #host and port as tuple

    displayOptions()
    opt = input("Enter your choice: ")

    while True:
        client_socket.send(opt.encode())
        match int(opt):
                
            case 1:
                data = client_socket.recv(1024).decode()
                contacts = json.loads(data)
                for i in sorted(contacts.keys()):
                    print(f"{i}:{contacts[i]}")
            case 2:
                data = client_socket.recv(1024).decode()
                name = input(data+":-")
                client_socket.send(name.encode())
                data = client_socket.recv(1024).decode()
                number = input(data + ":-")
                client_socket.send(number.encode())
            case 3:
                data = client_socket.recv(1024).decode()
                name = input(data + ":-")
                client_socket.send(name.encode())
                data = client_socket.recv(1024).decode()
                print(data)
            case 4:
                data = client_socket.recv(1024).decode()
                name = input(data + ":-")
                client_socket.send(name.encode())
                data = client_socket.recv(1024).decode()
                print(data)
            case 5:
                data = client_socket.recv(1024).decode()
                num = input(data + ":-")
                client_socket.send(num.encode())
                data = client_socket.recv(1024).decode()
                print(data)
            case 6:
                break

            case _:
                print("Wrong choice")

        displayOptions()
        opt = input("Enter your choice: ")
    
    client_socket.close()

if __name__ == '__main__':
    client()