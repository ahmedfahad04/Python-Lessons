# Single Threaded Echo Client

import socket
import argparse

host = 'localhost'

def echo_client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    sock.connect(server_address)

    try:

        # data -----
        f = open("a.txt", "r")
        message = f.read()

        # data -----
        # message = "Test message that will be echoed"
        print("[Client] Send:", message)
        sock.sendall(message.encode('utf-8'))  # *** WRITING ***

        data_received = 0
        data_expected = len(message)
        content = ''

        while data_received < data_expected:
            data = sock.recv(16)  # *** READING ***
            data_received += len(data)
            content += data.decode('utf-8')
            # print("[Client] Received:", data.decode('utf-8'))

    except socket.error as msg:
        print("[Client] Socket error: ", str(msg))

    except Exception as msg:
        print("[Client] Other exception: ", str(msg))

    finally:
        print("[Client] Full Message: ", content)
        print("[Client] Closing connection to the server")
        sock.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)
