import socket

HOST = 'localhost'
PORT = 5050

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(5)

    conn, addr = s.accept()
    print("Connection established from {}".format(addr))

    conn.send('1.Cong 2.Tru'.encode('utf-8'))
    response = conn.recv(1024).decode('utf-8')
    opt,a,b,c = response.split()
    if(opt == '1'):
        conn.send(str(int(a) + int(b) + int(c)).encode('utf-8'))
    elif(opt == '2'):
        conn.send(str(int(a) - int(b) - int(c)).encode('utf-8'))
    else:
        conn.send('Invalid request!'.encode('utf-8'))
    s.close()