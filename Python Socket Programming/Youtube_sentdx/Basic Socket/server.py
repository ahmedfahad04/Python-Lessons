import socket
import time

HEADERSIZE = 10

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5001))
server_socket.listen(10)

print("[LISTENING...] Server is listening on localhost:5000")

while True:
    client_socket, address = server_socket.accept()
    print(f'[Server] Connection from {address} has been established!')

    # MESSAGE READING STARTS
    file = open("demo.txt", "r")
    msg = file.read()
    # demoMESSAGE READING ENDS

    msg_length = f'{len(msg):<{HEADERSIZE}}'    # HEADER
    msg = msg_length + msg      # Actual Message with HEADER
   
    # WRITING END
    client_socket.send(bytes(msg, "utf-8"))

    while True:
        time.sleep(3)
        msg = f"The time is {time.ctime(time.time())}"
        msg = f"{len(msg):<{HEADERSIZE}}" + msg

        print(msg)

        client_socket.send(bytes(msg, "utf-8"))


    
