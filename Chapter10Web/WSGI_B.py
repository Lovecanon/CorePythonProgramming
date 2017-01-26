#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import ctime
from wsgiref.simple_server import make_server


# 中间件和封装wsgi应用

def simple_wsgi_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain; charset=utf-8')]
    start_response(status, headers)  # python3将原生字符串类型用于HTTP头和对应的元数据
    # 必须返回一个可迭代对象用于组成响应负载
    return [b'Hello World!', b'I\'m a bird']  # 元素为bytes类型用在HTTP负载(请求/响应/get\post数据/html输出3)


def ts_simple_wsgi_app(environ, start_response):
    return [b'[%b] %b\n' % (bytes(ctime(), encoding='utf-8'), x) for x in simple_wsgi_app(environ, start_response)]


class Ts_ci_wrapp(object):
    # timestamp callable instance wrapped application
    def __init__(self, app):
        self.orig_app = app

    def __call__(self, *args):
        # 且把call当作普通方法，如果call(111, 222)这样调用
        # *args: 111 222
        # args: ('111', '222')
        return [b'[%b] %b\n' % (bytes(ctime(), encoding='utf-8'), x) for x in self.orig_app(*args)]


http_d = make_server('localhost', 8080, Ts_ci_wrapp(simple_wsgi_app))
print('Started app serving on port 8080...')
http_d.serve_forever()
