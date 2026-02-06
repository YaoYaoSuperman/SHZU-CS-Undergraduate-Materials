import socket

def udp_client():
    host = 'localhost'
    port = 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            message = input("Enter your message: ")
            if message.lower() == 'exit':
                break
            client_socket.sendto(message.encode(), (host, port))
            data, server = client_socket.recvfrom(1024)
            print('Received from server:', data.decode())
    finally:
        client_socket.close()

if __name__ == '__main__':
    udp_client()
