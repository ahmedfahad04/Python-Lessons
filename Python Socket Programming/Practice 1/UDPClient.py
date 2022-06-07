from socket import *

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)  #AF_INET means IP version 4 & SOCK_DGRAM means is of UDP socket

while True:
    message = input("Enter a message with lowercase letters: ")
    
    if(message == "exit"): break
    
    clientSocket.sendto(message.encode(), (serverName, serverPort)) # message.encode() -> convert the string message to byte stream
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)    # 2048 is the buffer size for receving output from Server
    print("Server: ",modifiedMessage.decode())
        

clientSocket.close()
