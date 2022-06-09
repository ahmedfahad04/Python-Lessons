import socket
import time
import random
import pickle

HEADERSIZE = 10

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5001))
server_socket.listen(10)

print("[LISTENING...] Server is listening on localhost:5000")

while True:
    client_socket, address = server_socket.accept()
    print(f'[Server] Connection from {address} has been established!')

    # MESSAGE READING STARTS

    l = ['hello', 'people']
    msg = pickle.dumps(l)
    # demoMESSAGE READING ENDS

    msg_length = bytes(f'{len(msg):<{HEADERSIZE}}', 'utf-8') # HEADER
    msg = msg_length + msg  # Actual Message with HEADER

    # WRITING END
    client_socket.send(msg)



