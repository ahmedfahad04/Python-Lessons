import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = socket.gethostbyname(socket.gethostname())
port = 5050

server.bind((ip, port))
server.listen(10)

while True:
    client, addr = server.accept()
    print("[Server] Client connected from: ", addr)
    
    msglen = client.recv(1024)
    message = client.recv(int(msglen)).decode("utf-8")
    print(f"[Client] {message}")
    
    msg = "Hello Client!"
    client.send(msg.encode("utf-8"))