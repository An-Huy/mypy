import socket

HOST = 'localhost'
PORT = 5000

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((HOST,PORT))

    while True:
        msg = input("string(type quit to escape): ")
        s.sendto(msg.encode('utf-8'), (HOST, PORT))
        if msg == 'quit':   
            break
        data = s.recvfrom(1024)[0]
        print(data.decode('utf-8'))