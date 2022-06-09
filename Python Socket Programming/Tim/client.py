import socket

# constant values
DISCONNECT_MSG = "!DISCONNECT"
FORMATE = "utf-8"
HEADER = 65500
PORT = 5050
IP_ADDR = "127.0.1.1"
SERVER = (IP_ADDR, PORT)

# client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(SERVER)


def send():

    msg = input("[Client] Enter your message: ")

    while True:

        ### encode the message (WRITING END)
        message = msg.encode(FORMATE)
        msg_length = len(message)

        # encode message length
        send_length = str(msg_length).encode(FORMATE)

        # padding message length to 64 bytes
        send_length += b' ' * (HEADER - len(send_length))

        # finally send the data
        client.send(send_length)
        client.send(message)

        if msg == DISCONNECT_MSG:
            break

        ### (READING END)
        data = ''
        while True:
            content = client.recv(1024).decode(FORMATE)
            if len(content) <= 0:
                break
            
            data += content
            
        print("[Client Received:] ", data)
            
            
        msg = input("[Client] Enter your message: ")


if __name__ == '__main__':

    send()
