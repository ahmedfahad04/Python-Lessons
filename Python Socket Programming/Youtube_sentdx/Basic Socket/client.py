from http import client
import socket

HEADERSIZE = 10

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5001))


while True:
    content = ''
    new_msg = True
    msg_len = 0

    while True:

        # READING END
        msg = client_socket.recv(16)

        # MESSAGE SIZE
        if new_msg:
            msg_len = int(msg[:HEADERSIZE])
            new_msg = False

        content += msg.decode("utf-8")
        print("FULL MESSAGE LENGTH: ", len(content))

        # TERMINATION CONDITION
        if (len(content) - HEADERSIZE) == msg_len:
            print("FULL CONTENT RECEIVED")
            print("[Server] ", content[HEADERSIZE:])
            new_msg = True
            break

