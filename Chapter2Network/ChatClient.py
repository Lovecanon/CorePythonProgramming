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
        data_to_send = input('[Client]')
        if not data_to_send or data_to_send == 'exit':
            print('bye')
            break
        c_socket.send(data_to_send.encode())

        data = c_socket.recv(BUFFER_SIZE)
        print('[Server]', data)

    c_socket.close()