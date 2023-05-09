import socket

HOST = 'localhost'
PORT = 5000

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST,PORT))

    data, addr = s.recvfrom(1024)
    print(data.decode('utf-8'))
    s.sendto('1.Cong 2.Tru'.encode('utf-8'), addr)   

    response, addr = s.recvfrom(1024)
    value = response.decode('utf-8').split()
    if int(value[0]) == 1:
        msg = int(value[1]) + int(value[2]) + int(value[3])
    elif int(value[0]) == 2:
        msg = int(value[1]) - int(value[2]) - int(value[3])
    else:
        msg = 'Invalid request!'
    data = str(msg)
    s.sendto(data.encode('utf-8'), addr)