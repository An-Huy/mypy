import socket

host = 'localhost'
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

request = input("max or min: ")
s.sendall(request.encode('utf-8'))

msg = input("a,b: ")
s.sendall(msg.encode('utf-8'))

data = s.recv(1024).decode('utf-8')
print("data: %s" %data)