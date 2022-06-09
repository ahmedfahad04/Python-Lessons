import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
print("OLD STATE: ", old_state)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
new_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
print("NEW STATE: ", new_state)

local_port = 8282
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind(("127.0.0.1", local_port))
srv.listen(1)
print("Listening on port: %s " %local_port)

while True:
    try:
        client, addr = srv.accept()

    except KeyboardInterrupt:
        print("Key board Interrupt")
        break
    except socket.error as msg:
        print(f"Error: {msg}")



