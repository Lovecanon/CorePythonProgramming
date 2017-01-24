#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 55555
    BUFFER_SIZE = 1024
    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_socket.connect((HOST, PORT))

    while True:
        data = b'i am The Machine.i am The Machine.i am The Machine'
        c_socket.send(data)
        recv_data = c_socket.recv(BUFFER_SIZE)
        if not recv_data:
            break
        print(recv_data.decode('utf-8'))
        break
    c_socket.close()
