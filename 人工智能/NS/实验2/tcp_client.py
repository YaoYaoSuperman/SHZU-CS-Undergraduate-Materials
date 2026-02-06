import socket

def tcp_client():
    host = 'localhost'  # 服务器地址
    port = 12345        # 服务器端口

    # 创建socket对象
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接到服务器
    client_socket.connect((host, port))

    message = 'Hello, TCP Server!'
    try:
        # 发送数据
        client_socket.sendall(message.encode())
        # 接收回响数据
        data = client_socket.recv(1024)
        print('Received:', data.decode())
    finally:
        # 关闭连接
        client_socket.close()

if __name__ == '__main__':
    tcp_client()
