import socket

HOST = 'localhost'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)

conn = s.accept()[0]
request = conn.recv(1024).decode('utf-8')
numbers = conn.recv(1024).decode('utf-8')

try:
    a,b = numbers.split()
    if request == 'max':
        res = max(a,b)
    elif request == 'min':
        res = min(a,b)
    else:
        msg = 'Invalid request!!'
        conn.send(msg.encode('utf-8'))
    msg = str(res)
    conn.send(msg.encode('utf-8'))
except Exception as e:
    print('%s' %e)

s.close()