#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server, demo_app


def simple_wsgi_app(environ, start_response):
    # status = '200 OK'
    # headers = [('Content-Type', 'text/plain; charset=utf-8')]
    # start_response(status, headers)  # python3将原生字符串类型用于HTTP头和对应的元数据
    # 必须返回一个可迭代对象用于组成响应负载
    # return ['Hello World!'.encode('utf-8')]  # 元素为bytes类型用在HTTP负载(请求/响应/get\post数据/html输出3)

    # 下面是demo_app的源代码
    from io import StringIO
    stdout = StringIO()  # 很多时候，数据读写不一定是文件，也可以在内存中读写
    print("Hello world!", file=stdout)  # 将内存字符串"Hello world!"写入到StringIO对象中，使用getValue()获取
    print(file=stdout)  # 写入一个换行

    # 将environ环境变量输出给浏览器
    h = sorted(environ.items())
    for k, v in h:
        print(k, '=', repr(v), file=stdout)
    start_response("200 OK", [('Content-Type', 'text/plain; charset=utf-8')])
    return [stdout.getvalue().encode("utf-8")]


http_d = make_server('localhost', 8080, demo_app)
print('Started app serving on port 8080...')
http_d.serve_forever()