#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
from urllib.parse import quote_plus

header = 'Content-Type:text/html \n'
url = '/cgi-bin/FriendC.py'
error_html = '''
<html>
    <head>
        <title>Friends CGI Demo</title>
    </head>
    <body>
        <h3>ERROR</h3>
        <b>%s</b><p>
        <form>
            <input type = "button" value = "back" onclick="window.history.back()">
        </form>
    </body>
</html>
'''


def showError(error_str):
    print((header + error_html) % error_str)


form_html = '''
<html>
    <head>
        <title>Friends CGI Demo</title>
    </head>
    <body>
        <h3>Friends list for:<i>%s<i></h3>
    </body>
    <form action="%s">
        <b>Enter your name:</b>
        <input type = "hidden" name = "action" value = "edit">
        <input type = "text" name = "person" value = "%s" size = 15>
        <p><b>how many friends do you have?</b>
        %s
        <p><input type = "submit">
    </form>
</html>
'''
form_radio = '<input type = "radio" name = "howmany" value="%s" %s> %s\n'


def showForm(who, howmany):
    friends = []
    for i in (0, 10, 25, 50, 100):
        checked = ''
        if str(i) == howmany:
            checked = "checked"
        friends.append(form_radio % (str(i), checked, str(i)))
    print('%s%s' % (header, form_html % (who, url, who, ''.join(friends))))


response_html = '''
<html>
    <head>
        <title>Friends CGI Demo</title>
    </head>
    <body>
        <h3>Friends list for:<i>%s</i></h3>
        your name is:<b>%s</b><p>
        you have <b>%s </b>friends.
        <p>Click <a href='%s'>here</a> to edit your data again
    </body>
</html>
'''


def doResults(who, howmany):
    newurl = (url + ('?action = reedit&person=%s&howmany=%s') % (quote_plus(who), howmany))
    print((header + response_html) % (who, who, howmany, newurl))


def process():
    error = ''
    form = cgi.FieldStorage()

    if 'person' in form:
        who = form['person'].value.title()
    else:
        who = 'new user'

    if 'howmany' in form:
        howmany = form['howmany'].value
    else:
        if 'action' in form and form['action'].value == 'edit':
            error = 'please select number of friemds.'
        else:
            howmany = 0
    if not error:
        # 1.如果没有error
        # 1.1.返回处理结果页面
        # 1.2.返回表格页面
        if 'action' in form and form['action'].value != 'reedit':
            doResults(who, howmany)
        else:
            showForm(who, howmany)
    else:
        # 2.如果存在error
        showError(error)


if __name__ == '__main__':
    process()
