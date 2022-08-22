from ast import match_case
import socket
import json


def display():
    return ''' 
    MENU :   
    1. List all contacts
    2. Add new contact
    3. Delete contact
    4. Search contact by name
    5. Search contact by number
    6. Exit\n'''

phone_number = {}

def server():
    found = False
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostname = socket.gethostname()
    port = 12345
    print(hostname)
    s.bind((hostname, port))
    s.listen(3)
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send('Welcome to the phone book server\n'.encode())
    c.send(display().encode())
    while True:
        data = c.recv(1024).decode()
        data = json.loads(data)
        if data['opt'] == '1':
            pass
        elif data['opt'] == '2':
            name = data['name']
            number = data['phone_number']
            phone_number[name] = data['phone_number']
            with open('phone_book.txt', 'a') as f:
                f.write(name + ' ' + number + '\n')
            c.send('Contact {} {} added successfully\n'.format(name, number).encode())
        elif data['opt'] == '3':
            pass
            

            #print("Msg from Client: ",str(addr),"-", str(data))
            
            #c.send(data.encode())
    c.close()

if __name__ == '__main__':
    server()