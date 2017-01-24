#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

if __name__ == '__main__':
    # 半双工聊天：两个人聊天，一人一句话。
    #

    HOST = '127.0.0.1'
    PORT = 55555
    BUFFER_SIZE = 1024
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.bind((HOST, PORT))
    s_socket.listen(5)

    while True:
        print('waiting for connection...')
        c_socket, address = s_socket.accept()
        print('connect address:', address)
        while True:
            data = c_socket.recv(BUFFER_SIZE)
            if not data:
                break
            print('[Client] ', data)

            data_to_send = input('[Server] ')
            if not data_to_send or data_to_send == 'exit':
                print('bye')
                break
            c_socket.send(data_to_send.encode())

        c_socket.close()
    s_socket.close()



