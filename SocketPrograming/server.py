import socket

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostname = socket.gethostname()
    port = 12345
    print(hostname)
    s.bind((hostname, port))
    s.listen(2)
    c, addr = s.accept()
    print('Got connection from', addr)
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        else:
            print("Msg from Client: ",str(addr),"-", str(data))
            data = input("Enter MSG:")
            c.send(data.encode())
    c.close()

if __name__ == '__main__':
    server()