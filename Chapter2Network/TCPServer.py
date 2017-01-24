#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
from time import ctime

if __name__ == '__main__':
    # 功能：客户端发送数据给服务器。服务器将数据添加一个时间戳再发送给客户端。
    # 问题：如果客户端以BUFFER_SIZE=1024发送数据，服务器端以BUFFER_SIZE=5接收数据,
    # 服务器端如何知道数据接收完成该发送数据给客户端?(数据>5byte)
    #

    HOST = '127.0.0.1'
    PORT = 55555
    BUFFER_SIZE = 1024
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.bind((HOST, PORT))
    s_socket.listen(5)
    while True:
        print('Waiting for connection...')
        c_socket, c_address = s_socket.accept()
        print('connected from:', c_address)
        while True:
            print('start receive')
            recv_data = c_socket.recv(BUFFER_SIZE)
            print('server receive:', recv_data)
            if not recv_data:  # 如果没有数据终止循环
                print('break')
                break
            c_socket.send(b'[%s] %s' % (bytes(ctime(), 'utf-8'), recv_data))
        c_socket.close()
    s_socket.close()
