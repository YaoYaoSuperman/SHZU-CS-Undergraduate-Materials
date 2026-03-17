import socket

def tcp_server():
    host = 'localhost'
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print('TCP Server is listening on port', port)

    conn, addr = server_socket.accept()
    print('Connected by', addr)

    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print('Received:', data.decode())
            response = input("Enter your response: ")  # 允许服务器管理员输入响应
            conn.sendall(response.encode())  # 发送响应回客户端
    finally:
        conn.close()

if __name__ == '__main__':
    tcp_server()
