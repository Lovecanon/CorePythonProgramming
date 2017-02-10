#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ftplib import FTP
from ftplib import error_perm
import socket
import os

HOST = 'qxw1146830262.my3w.com'
DIR = 'Hello'
DOWNLOAD_FILE = '01.txt'
UPLOAD_FILE = 'FTP.py'
USERNAME = 'qxw1146830262'


def main():
    # 使用FTP进行上传下载文件
    # 1. 创建FTP对象
    try:
        f = FTP(HOST)
    except (socket.error, socket.gaierror) as e:
        print('ERROR: Cannot reach "%s".' % (HOST,))
        return
    print('*** Connected to host "%s".' % (HOST,))

    # 2. 尝试使用用户名密码登陆FTP服务器
    try:
        f.login(USERNAME, '******')
    except error_perm as e:
        print('ERROR: Cannot login.')
        f.quit()
        return
    print('*** Logged in as "%s".' % (USERNAME,))

    # 3. 转到目标目录
    try:
        f.cwd(DIR)
    except error_perm as e:
        print('ERROR: Cannot cd to "%s".' % (DIR,))
        f.quit()
        return
    print('*** Changed to "%s" folder.' % (DIR,))

    # 4.下载目标目录中的文件到本地
    try:
        f.retrlines('RETR %s' % (DOWNLOAD_FILE,), open(DOWNLOAD_FILE, 'w').write)
    except error_perm:
        print('ERROR: Cannot read file "%s".' % (DOWNLOAD_FILE,))
        os.unlink(DOWNLOAD_FILE)
    print('*** Download "%s" success.' % (DOWNLOAD_FILE,))

    # 5.上传文件到FTP服务器中
    # 注：第一个参数是命令符
    # 第二个参数是文件对象；必须用二进制文件格式进行打开文件
    try:
        f.storlines('STOR %s' % (UPLOAD_FILE,), open(UPLOAD_FILE, 'rb'))
    except error_perm:
        print('ERROR: Cannot upload file "%s".' % (UPLOAD_FILE,))
    print('*** Upload "%s" success.' % (UPLOAD_FILE,))

    f.quit()

if __name__ == '__main__':
    main()
