import socket
import ssl
import argparse
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

def send_request(domain, port, ssl_enabled, method, endpoint, http_version, log_file=None):
    # create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if ssl_enabled:
        # wrap the socket with SSL
        client_socket = ssl.wrap_socket(client_socket)

    # connect to the server
    client_socket.connect((domain, port))

    # send the HTTP request
    request = f'{method} {endpoint} {http_version}\r\n\r\n'.encode()
    print(f'[+] REQUEST:\n{request}\n')
    client_socket.sendall(request)

    # receive the response from the server
    response = client_socket.recv(4096)

    # close the socket connection
    client_socket.close()

    # print the response
    print(f'[+] RESPONSE:\n{response.decode()}')

    # write the response to a log file if specified
    if log_file:
        with open(log_file, 'w') as f:
            f.write(response.decode())


def main():
    parser = argparse.ArgumentParser(description='Send a raw HTTP request to a server and check the Location for the internal IP leak.')
    parser.add_argument('-d', '--domain', required=True, help='The domain or IP address of the server')
    parser.add_argument('-p', '--port', required=True, type=int, help='The port number to connect to')
    parser.add_argument('-s', '--ssl', action='store_true', help='Use SSL for HTTPS requests')
    parser.add_argument('-m', '--method', default='GET', help='The HTTP method to use')
    parser.add_argument('-e', '--endpoint', default='/', help='The endpoint to request')
    parser.add_argument('-o', '--output', help='Save the response to a log file')
    parser.add_argument('-v', '--version', default='HTTP/1.0', help='The HTTP version to use')

    args = parser.parse_args()

    send_request(args.domain, args.port, args.ssl, args.method, args.endpoint, args.version, args.output)


if __name__ == '__main__':
    main()
