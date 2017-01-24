#!/usr/bin/env python
# -*- coding: utf-8 -*-
from atexit import register
from threading import Thread
from time import ctime
from urllib import request
from concurrent.futures import ThreadPoolExecutor
import re

RANK_PATTERN = '</span>\n(\d+)\n</span>'
AMAZON = 'https://www.amazon.cn/dp/'
ASIN = {
    'B01FQAS0KK': 'Python核心编程',
    'B00WKR1OKG': 'Python Cookbook(第3版)(中文版)',
    'B004TUJ7A6': 'Python学习手册'
}


def get_rank(asin):
    req = request.Request('%s%s' % (AMAZON, asin))
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    data = request.urlopen(req).read().decode('utf-8')
    return re.findall(RANK_PATTERN, data)[0]


def show_rank(asin):
    print('- %r ranked %s' % (ASIN[asin], get_rank(asin)))


def main():
    # 只有在I/O密集型的应用才能更好的发挥Python的并发性
    # 本例查询三本书在亚马逊上的排名。分别使用三个线程同时进行查询，速度会很快
    print('Visit Amazon at:', ctime())
    for asin in ASIN.keys():
        # show_rank(asin)  # 第一种：普通的调用方式，一本查询完成之后查询第二本
        Thread(target=show_rank, args=(asin,)).start()  # 第二种：使用多线程查询


def main_thread_pool():
    # 第三种：传递3设置线程池大小，得到执行器之后，他负责调度任务和整理结果
    print('Visit Amazon at:', ctime())
    with ThreadPoolExecutor(3) as executor:
        for asin in ASIN.keys():
            executor.submit(show_rank, asin)


@register
def at_exit():
    # @register注解会在Python解释器中注册一个退出函数，即在脚本退出之前调用这个函数
    print('All done at:', ctime())


if __name__ == '__main__':
    # main()
    main_thread_pool()
