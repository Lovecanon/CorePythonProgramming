#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server, demo_app


# WSGI是一个规范，其应用是可调用对象，参数为固定的两个。定义了Web服务器如何与Python应用程序进行交互，
# 使得使用Python写的Web应用程序可以和Web服务器对接起来。

# WSGI相当于是Web服务器和Python应用程序之间的桥梁。那么这个桥梁是如何工作的呢？首先，我们明确桥梁的作用，WSGI存在的目的有两个：
# 1.让Web服务器知道如何调用Python应用程序，并且把用户的请求告诉应用程序。
# 首先，每个application的入口只有一个，也就是所有的客户端请求都同一个入口进入到应用程序。
#
# 接下来，server端需要知道去哪里找application的入口。这个需要在server端指定一个Python模块，也就是Python应用中的一个文件，并且这个模块中需要包含一个名称为application的可调用对象（函数和类都可以），这个application对象就是这个应用程序的唯一入口了。WSGI还定义了application对象的形式：
#
# def simple_app(environ, start_response):
#       pass
# 2.让Python应用程序知道用户的具体请求是什么，以及如何返回结果给Web服务器。
def simple_wsgi_app(environ, start_response):
    # status = '200 OK'
    # headers = [('Content-Type', 'text/plain; charset=utf-8')]
    # start_response(status, headers)  # python3将原生字符串类型用于HTTP头和对应的元数据
    # 必须返回一个可迭代对象用于组成响应负载
    # return ['Hello World!'.encode('utf-8')]  # 元素为bytes类型用在HTTP负载(请求/响应/get\post数据/html输出3)

    # 下面是demo_app的源代码
    from io import StringIO
    stdout = StringIO()  # 很多时候，数据读写不一定是文件，也可以在内存中读写
    print("+++Hello world!", file=stdout)  # 将内存字符串"Hello world!"写入到StringIO对象中，使用getValue()获取
    print(file=stdout)  # 写入一个换行

    # 将environ环境变量输出给浏览器
    h = sorted(environ.items())
    for k, v in h:
        print(k, '=', repr(v), file=stdout)
    start_response("200 OK", [('Content-Type', 'text/plain; charset=utf-8')])
    return [stdout.getvalue().encode("utf-8")]


http_d = make_server('localhost', 8080, simple_wsgi_app)
# http_d = make_server('localhost', 8080, demo_app)  # 也可以使用示例给出的可调用对象
print('Started app serving on port 8080...')
http_d.serve_forever()