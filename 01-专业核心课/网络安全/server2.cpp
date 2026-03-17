#include<winsock2.h>
#include<stdio.h>
#include<iostream>
using namespace std;
int main() {
  SOCKET server_sockfd, client_sockfd;
  int server_len, client_len;
  struct sockaddr_in server_address;
  struct sockaddr_in client_address;
 
  // 注册 Winsock DLL
  WSADATA wsadata;
  if(WSAStartup(0x101,(LPWSADATA)&wsadata) != 0) {
    printf("Winsock 错误\n");
    exit(1);                                         
  }
 
  // 初始化 server socket
  server_sockfd = socket(AF_INET, SOCK_STREAM, 0); // AF_INET(使用IPv4); SOCK_STREAM; 0(使用缺省方式TCP)
  if(server_sockfd == SOCKET_ERROR) {
    printf("Socket 错误\n");
    exit(1);
  }
   
  server_address.sin_family = AF_INET; // AF_INT(使用IPv4)
  server_address.sin_addr.s_addr = inet_addr("127.0.0.1"); // ip地址为本机 
  server_address.sin_port = 9000; //必须是本机没有使用的端口号 
  server_len = sizeof(server_address);
  
  if(bind(server_sockfd, (struct sockaddr *)&server_address, server_len) < 0) {
    printf("绑定错误\n");
    exit(1);
  }

  if(listen(server_sockfd, 5) < 0) {
    printf("侦听错误\n");
    exit(1);
  }
 
  while(1) {
    char ch[1024]; //接收缓存 
    printf("服务器端启动，等待客户端发送消息中...\n");
    client_len = sizeof(client_address);

    client_sockfd = accept(server_sockfd, (struct sockaddr *)&client_address, &client_len);
    if(client_sockfd == SOCKET_ERROR) {
      printf("Accept Error\n");
      exit(1);
    }

    int mess=recv(client_sockfd, ch, 1024, 0); 
    
    for(int i=0;i<mess;i++) cout<<ch[i];
    cout<<endl;
    
    string backmessage="Received client message" ;
    send(client_sockfd, backmessage.c_str(), backmessage.length(), 0); 
    closesocket(client_sockfd); 
  }
}
