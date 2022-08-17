from ast import match_case
import socket

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
    while True:
        #print("After true")
        c.send(display().encode())
        #print("after send")
        #c.send('Enter your choice:'.encode())
        data = c.recv(1024).decode()
        print(data)
        if not data:
            break
        else:
            match(data):
                case '1':
                    text_data = ''''''
                    '''List all contacts'''
                    with open ('phone_book.txt', 'r') as f:
                        for line in f:
                            #print(line)
                            text_data += line
                        text_data += '''\n====================================\n'''
                        c.send(text_data.encode())
                        
                case '2':
                    '''Add a new contact'''
                    c.send('Enter name:'.encode())
                    name = c.recv(1024).decode()
                    c.send('Enter phone number:'.encode())
                    phone_number = c.recv(1024).decode()
                    with open('phone_book.txt', 'a') as f:
                        f.write(name + ' ' + phone_number + '\n')
                    c.send("Contact {} : {} added to phone book".format(name,phone_number).encode())
                case '3':
                    '''Delete a contact'''
                    c.send("1: Delete a contact by name".encode())
                    c.send("2: Delete a contact by number".encode())
                    opt = c.recv(1024).decode()
                    if opt == '1':
                        name = input("enter name to delete :")
                        with open('phone_book.txt', 'r+') as f:
                            for line in f:
                                if name not in line:
                                    f.write(line)
                            c.send("contact {} deleted!...".format(name).encode())
                    elif data == '2':
                        number = input("Enter phone number to delete:")
                        with open('phone_book.txt', 'r+') as f:
                            for line in f:
                                if number not in line:
                                    f.write(line)
                            c.send("number {} deleted!...".format(number).encode())
                    else:
                        c.send("Invalid option".encode())
                case '4':
                    '''seach by contact by name'''
                    found = False
                    name = input("Enter name to search: ")
                    with open ('phone_book.txt', 'r') as f:
                        for line in f:
                            if name in line:
                                found = True
                                c.send(line.encode())
                        if(not found):
                            c.send("contact not found".encode())
                case '5':
                    found = False
                    '''search by contact by number'''
                    number = input("Enter phone number:")
                    for line in f:
                        if number in line:
                            found = True
                            c.send(line.encode())
                    if(not found):
                        c.send("contact not found".encode())
                case '6':
                    print("Program Exited!")
                    break
                case '-':
                    print("Invalid option")
                    break
            

            #print("Msg from Client: ",str(addr),"-", str(data))
            
            #c.send(data.encode())
    c.close()

if __name__ == '__main__':
    server()