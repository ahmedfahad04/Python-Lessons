from http import server
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("Waiting for Clients...")

while True:
    
    message, clientAddress = serverSocket.recvfrom(2048)
    print("Client Connected!! ", clientAddress)
    print("Client: ",  message.decode())
    
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
