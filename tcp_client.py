"""
tcp客户端
"""
import socket

sockfd=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

server_addr=('127.0.0.1',8888)
# 连接服务端程序
sockfd.connect(server_addr)
while True:
    mes=input('>>')
    if not mes:
        break
    sockfd.send(mes.encode('utf-8'))
    data=sockfd.recv(1024)
    print(data.decode('utf-8'))

sockfd.close()