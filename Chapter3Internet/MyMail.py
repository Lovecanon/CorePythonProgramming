#!/usr/bin/env python
# -*- coding: utf-8 -*-
from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTP_SERVER = 'smtp.163.com'
POP_SERVER = 'pop.qq.com'
who = 'bboyxiangkai@163.com'
password = '***'
to_who = '535036628@qq.com'


def send_mail():
    # 如果主题和正文不加空行，邮件可以发送但不没有正文
    body = '''\
    From: %s
    To: %s
    Subject: immortalbird@sohu.com

    please tell me why?immortalbird@sohu.com
    ''' % (who, to_who)

    send_server = SMTP(SMTP_SERVER)
    send_server.login(who, password)
    errs = send_server.sendmail(who, [to_who], body)
    send_server.quit()
    assert len(errs) == 0, errs


def read_mail():
    receive_server = POP3(POP_SERVER)
    receive_server.user('immortalbird@sohu.com')
    receive_server.pass_(password)
    msg_ct, mbox_size = receive_server.stat()
    print(msg_ct, '--', mbox_size)
    rsp, msg_list, rsp_size = receive_server.retr(msg_ct)
    print(msg_list[0:])


if __name__ == '__main__':
    send_mail()