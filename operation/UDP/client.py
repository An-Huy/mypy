import socket

HOST = 'localhost'
PORT = 5000

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        r = input("Nhập 'r' để connect: ")
        if(r == 'r'):
            break
    s.sendto('Hello server'.encode('utf-8'), (HOST,PORT))
    
    data, addr = s.recvfrom(1024)
    print(data.decode('utf-8'))
    
    data = input("Nhập opt, a, b, c: ")
    s.sendto(data.encode('utf-8'), (HOST,PORT))
    
    data, addr = s.recvfrom(1024)
    print('Result: ', data.decode('utf8'))
