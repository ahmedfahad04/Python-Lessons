import socket
import threading

# constant values
DISCONNECT_MSG = "!DISCONNECT"
FORMATE = "utf-8"
HEADER = 64
PORT = 5050
IP_ADDR = socket.gethostbyname(socket.gethostname())
SERVER = (IP_ADDR, PORT)

# server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(SERVER)


def handle_client(client_object, address):
    
    print(f"[NEW CONNECTION] {address} connected.")
    
    connected = True
    
    while connected:
        messageLen = client_object.recv(HEADER)
        
        if messageLen:
            
            messageLen = int(messageLen)
            msg = client_object.recv(messageLen).decode(FORMATE)
            
            if msg == DISCONNECT_MSG:
                connected = False
                
            print(f"[{address}] {msg}")
        
    client_object.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    
    while True:
        client_object, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_object, address))
        thread.start()
        
        print(f"[Active Connection] {threading.activeCount() - 1}") 
        

print("[STARTING] Server is starting...")
start()