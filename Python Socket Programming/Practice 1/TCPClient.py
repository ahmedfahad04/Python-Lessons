from socket import *

while True: 
    
    serverName = "127.0.0.1"
    serverPort = 12500
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # print("Client Conncected!!")

    clientSocket.connect((serverName, serverPort))  # Before sending the message we need to ESTABLISH A CONNECTION
    
    # Before sending any message you must ESTABLISH connection
    message = input("Enter your message: ")
    if message == "exit": break
    
    clientSocket.send(message.encode())
    modifiedMessage = clientSocket.recv(1024)
    print("Server: ", modifiedMessage.decode())

    clientSocket.close()