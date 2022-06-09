import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
port = 5050

client.connect((host, port)) 

while True:
    
    data = client.recv(1024)
    print("[Server] ",  data.decode("utf-8"))
    
    
    client.send("Hi Server!".encode("utf-8"))
