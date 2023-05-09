import socket

HOST = 'localhost'
PORT = 5050

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        r = input("Nhập 'r' để connect: ")
        if(r == 'r'):
            break
    s.connect((HOST, PORT))

    data = s.recv(1024).decode('utf-8')
    print(data)
    request = input('Nhap opt, a, b, c: ')
    s.send(request.encode('utf-8'))

    result = s.recv(1024).decode('utf-8')
    print(result)