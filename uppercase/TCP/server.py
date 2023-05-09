import socket

HOST = 'localhost'
PORT = 5000

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(5)

    conn = s.accept()[0]
    while True:
        data = conn.recv(1024).decode('utf-8')
        if data == 'quit':
            break

        count = 0
        for i in data:
            if i.isupper():
                count += 1
        res = str(count)
        conn.send(res.encode('utf-8'))