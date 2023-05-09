import socket

HOST = 'localhost'
PORT = 5000

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST,PORT))

    while True:
        data, addr = s.recvfrom(1024)
        if data.decode('utf-8') == 'quit':
            break

        count = 0
        for i in data.decode('utf-8'):
            if i.isupper():
                count += 1
        res = str(count)
        s.sendto(res.encode('utf-8'), addr)