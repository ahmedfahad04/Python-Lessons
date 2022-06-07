import socket

# constant values
DISCONNECT_MSG = "!DISCONNECT"
FORMATE = "utf-8"
HEADER = 64
PORT = 5050
IP_ADDR = "127.0.1.1"
SERVER = (IP_ADDR, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(SERVER)

