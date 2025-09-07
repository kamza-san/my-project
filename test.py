import socket

host = "127.0.0.1"
port = 5555

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((host, port))
print("connected to server!")