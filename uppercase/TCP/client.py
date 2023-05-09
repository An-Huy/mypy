import socket

HOST = 'localhost'
PORT = 5000

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))

    while True:
        msg = input("string(type quit to escape): ")
        s.send(msg.encode('utf-8'))
        if msg == 'quit':   
            break
        data = s.recv(1024).decode('utf-8')
        print(data)
    s.close()