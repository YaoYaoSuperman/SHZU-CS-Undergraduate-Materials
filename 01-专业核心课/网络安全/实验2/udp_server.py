import socket

def udp_server():
    host = 'localhost'
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print('UDP Server is listening on port', port)

    try:
        while True:
            data, addr = server_socket.recvfrom(1024)
            print('Received from', addr, ':', data.decode())
            response = input("Enter your response: ")
            server_socket.sendto(response.encode(), addr)
    finally:
        server_socket.close()

if __name__ == '__main__':
    udp_server()
