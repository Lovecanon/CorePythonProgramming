#!/usr/bin/env python
# -*- coding: utf-8 -*-
from http.server import CGIHTTPRequestHandler, test
# 1.启动一个最基本的web服务器 + 已编写好的应用程序
# 2.Chrome访问：http://localhost:8080/friends.html并填写表格数据，会提交给cgi-bin/FriendA.py处理
# 3.FriendA.py中提交过来的表单是一个FieldStorage的实例，获取表单数据再返回新的HTML正文
test(CGIHTTPRequestHandler, port=8080)
