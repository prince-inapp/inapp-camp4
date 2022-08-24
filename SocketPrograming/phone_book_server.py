import json
import socket

phoneBook = dict()

def server():
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host,port))
    server_socket.listen(2) 

    conn, address = server_socket.accept()
    opt = ''
    found = False
    while(True):
        
        data = conn.recv(1024).decode()
        opt = data

        match int(opt):
            case 1:
                phoneBookJson = json.dumps(phoneBook)
                conn.send(phoneBookJson.encode())
            case 2:
                conn.send("Enter Name: ".encode())
                name = conn.recv(1024).decode()
                conn.send("Enter Number: ".encode())
                number = conn.recv(1024).decode()
                phoneBook[name] = number
            case 3:
                conn.send("Enter Name: ".encode())
                name = conn.recv(1024).decode()
                if name in phoneBook:
                    del phoneBook[name]
                    conn.send("Contact Deleted".encode())
                else:
                    conn.send("Name not found".encode())
            case 4:
                conn.send("Enter Name: ".encode())
                name = conn.recv(1024).decode()
                if name in phoneBook:
                    result = f"{name} : {phoneBook[name]}"
                else:
                    result = "Not Found"
                conn.send(result.encode())
            case 5:
                conn.send("Enter Number: ".encode())
                number = conn.recv(1024).decode()
                for name in phoneBook:
                    if phoneBook[name] == number:
                        result = f"{name} : {phoneBook[name]}"
                        conn.send(result.encode())
                        found = True
                        break
                if not found:
                    conn.send("Not Found".encode())
            case 6:
                break

            case _:
                result = "Wrong choice"
                conn.send(result.encode())
    conn.close() 
if __name__ == '__main__':
    server()
