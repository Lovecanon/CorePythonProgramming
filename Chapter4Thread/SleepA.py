#!/usr/bin/env python
# -*- coding: utf-8 -*-
import _thread
from time import ctime, sleep


def loop0():
    print('start loop 0 at:', ctime())
    sleep(4)
    print('end loop 0 at:', ctime())


def loop1():
    print('start loop 1 at:', ctime())
    sleep(2)
    print('end loop 1 at:', ctime())


def main():
    # 使用_thread模块,两个循环是并发执行的(很明显，短的那个先结束)，运行时间和最慢的那个有关
    # sleep(6)作用：如果不阻止主线程，他将会执行下一条语句然后结束程序。使用_thread模块，主线程
    # 不管其他线程的死活，自己执行完毕程序就结束。
    print('Starting at:', ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    sleep(6)
    print('All Done at:', ctime())


if __name__ == '__main__':
    main()
