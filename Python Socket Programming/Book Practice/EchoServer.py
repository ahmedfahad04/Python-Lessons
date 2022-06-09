# Single Threaded Echo Server

import socket
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5


def echo_server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # create SOCKET
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reuse ADDRESS
    server_address = (host, port)       # pair of host and port
    sock.bind(server_address)           # bind host and port
    sock.listen(backlog)                # set client listen count

    print(f"[Server] Starting Echo server on {host} port {port}")

    while True:
        print("[Listening...] Waiting to receive message from clients")

        client, addr = sock.accept()        # accept client request
        data = client.recv(data_payload)    # **** READING ****

        if data:
            print("[Server] Data: ", data.decode('utf-8'))

            # modify data --
            data = data.decode('utf-8')
            data = str(len(data)) + " --- " + str(data)
            # modify data --

            client.send(data.encode('utf-8'))  # **** WRITING ****
            print(f"[Server] Sent: {data} bytes back {addr}")

        client.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)
