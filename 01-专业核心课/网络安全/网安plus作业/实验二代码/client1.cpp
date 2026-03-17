#include<winsock2.h>
#include<stdio.h>
#include<iostream>
using namespace std;

int main() {

  SOCKET sockfd;
  int len;
  struct sockaddr_in address;
  int result;
    
  WSADATA wsadata;
  if(WSAStartup(0x101,(LPWSADATA)&wsadata) != 0) {
    printf("Winsock Error\n"); 
    exit(1);
  }
  sockfd = socket(AF_INET, SOCK_STREAM, 0);
  address.sin_family = AF_INET;
  address.sin_addr.s_addr = inet_addr("127.0.0.1");
  address.sin_port = 9000;
  len = sizeof(address);
 
  result = connect(sockfd, (struct sockaddr *)&address, len);  
  if(result == -1) {
    printf("Connetc Error");
    exit(1);
  }
  
 
  
cout<<"this is client!"<<endl;
  string inpu;
  cin>>inpu;
 
  if (inpu=="end!")
  {exit(0);}
  else
  {
  send(sockfd, inpu.c_str(), inpu.length(), 0);
  }
    
  char ba[1024];
  int reclen=recv(sockfd, ba, 1024, 0);
  for(int i=0;i<reclen;i++) cout<<ba[i];
  cout<<endl;

closesocket(sockfd);
 exit(0); 
}
