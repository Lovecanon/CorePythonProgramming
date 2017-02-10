#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi

# 必须先启动web服务器。而本py文件是应用程序
# 头文件和html正文之间有个空行
response_html = ''' Content-type:text/html \r\n
<html>
    <head>
        <title>Friends CGI demo(dynamic screen)</title>
    </head>
    <body>
        <h3>Friends list for:<i>%s</i></h3>
        your name is :<b>%s</b><p>
        you have <b>%s </b>friends.
    </body>
</html>
'''
form = cgi.FieldStorage()
who = form['person'].value
howmany = form['howmany'].value
print(response_html % (who, who, howmany))
