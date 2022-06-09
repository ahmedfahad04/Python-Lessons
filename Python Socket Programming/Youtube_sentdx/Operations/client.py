import pickle
import socket

HEADERSIZE = 10

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5001))


while True:
    content = b''
    new_msg = True
    msg_len = 0

    while True:

        # READING END
        msg = client_socket.recv(16)
        # print(f"[SERVER] {msg}")

        # MESSAGE SIZE
        if new_msg:
            msg_len = int(msg[:HEADERSIZE].decode('utf-8'))
            new_msg = False

        content += msg
        # print("FULL MESSAGE LENGTH: ", len(content))

        # TERMINATION CONDITION
        if (len(content) - HEADERSIZE) == msg_len:
            print("FULL CONTENT RECEIVED")
            print("[Server] ", content[HEADERSIZE:])
            print(pickle.loads(content[HEADERSIZE:]))
            new_msg = True
            content = b''

