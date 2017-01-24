#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib import request

if __name__ == '__main__':
    # 返回一个文件对象f，可以调用f读取的各种方法
    f = request.urlopen('http://www.baidu.com')
    print(f.readline())
    print(f.readline())
    f.close()

    # 将页面下载到index.html文件中,返回文件名和Web服务器响应后返回的MIME文件头
    file_name, mime_hdrs = request.urlretrieve('http://www.baidu.com', './index.html')
    print(file_name)
    print(mime_hdrs)
