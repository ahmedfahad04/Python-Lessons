from email.header import Header
import socket
import threading

# constant values
DISCONNECT_MSG = "!DISCONNECT"
FORMATE = "utf-8"
HEADER = 65500
PORT = 5050
IP_ADDR = socket.gethostbyname(socket.gethostname())
SERVER = (IP_ADDR, PORT)

# server socket 1
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(SERVER)


def handle_client(client_object, address):
    
    print(f"\n[NEW CONNECTION] {address} connected.")
    connected = True
    
    while connected:
        
        ### received data (READING END)
        # this statement is important, because through this statement,
        # we'll know the data size form it's header file
        messageLen = client_object.recv(HEADER)
        
        if messageLen:
            
            # get the length of the message
            # messageLen = int(messageLen)
            msg = client_object.recv(HEADER).decode(FORMATE)
            
            # terminating condition
            if msg == DISCONNECT_MSG:
                connected = False
                break
            
            ### (WRITING END)
            
            try:
                filename = "Tim/"+msg
                file = open(filename, "r")
            except:
                file = open(filename, "w+")
                print(f"[FILE] {filename} created.")
        
            content = file.read(1024)
            
            while content:
                client_object.send(content.encode(FORMATE))
                print(f"[SENT] {content}")
                content = file.read(1024)   # read the file by 1024 bytes
                           
            print(f"[{address}] {msg}")
        
    print(f"[DISCONNECTED] {address}")
    client_object.close()
        

def start():
    
    # start listening for connections 2
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    
    while True:
        
        # accept a connection 3
        client_object, address = server.accept()
        
        # start a thread for the client
        thread = threading.Thread(target=handle_client, args=(client_object, address))
        thread.start()
        
        # print the address of the client
        print(f"[Active Connection] {threading.activeCount() - 1}") 
        

if __name__ == '__main__':
    
    
    print("[STARTING] Server is starting...")
    start()