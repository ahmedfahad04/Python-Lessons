from socket import *

serverPort = 12500
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)  # maximum number of queued connection (here is at least 1)
print("Waiting for Clients...")

while True:
    
    # when client try to connect with server this accept() method is invoked
    # then a dedicated connection Socket is created for that particular client
    connectionSocket, addr = serverSocket.accept() 
    print("Client Connected!!", addr)
    
    message = connectionSocket.recv(1024).decode().upper()
    connectionSocket.send(message.encode())
    connectionSocket.close()
    
    