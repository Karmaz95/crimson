import socket
import ssl
import argparse
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def send_request(domain, port, ssl_enabled, log_file=None):
    # create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if ssl_enabled:
        # wrap the socket with SSL
        client_socket = ssl.wrap_socket(client_socket)

    # connect to the server
    client_socket.connect((domain, port))

    # send the HTTP request
    request = b'GET / HTTP/1.0\r\n\r\n'
    client_socket.sendall(request)

    # receive the response from the server
    response = client_socket.recv(4096)

    # close the socket connection
    client_socket.close()

    # print the response
    print(response.decode())

    # write the response to a log file if specified
    if log_file:
        with open(log_file, 'w') as f:
            f.write(response.decode())


def main():
    parser = argparse.ArgumentParser(description='Send a raw GET / HTTP/1.0 request to a server and check the Location for the internal IP leak.')
    parser.add_argument('-d', '--domain', required=True, help='The domain or IP address of the server')
    parser.add_argument('-p', '--port', required=True, type=int, help='The port number to connect to')
    parser.add_argument('-s', '--ssl', action='store_true', help='Use SSL for HTTPS requests')
    parser.add_argument('-o', '--output', help='Save the response to a log file')

    args = parser.parse_args()

    send_request(args.domain, args.port, args.ssl, args.output)


if __name__ == '__main__':
    main()
