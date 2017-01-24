#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
from time import sleep, ctime

loops = [4, 2]


def loop(n_loop, sleep_time):
    print('start loop ', n_loop, ' at:', ctime())
    sleep(sleep_time)
    print('end loop ', n_loop, ' at:', ctime())


def main():
    # 创建Thread的实例之传给他一个函数
    print('Start at:', ctime())
    threads = []
    n_loops = range(len(loops))
    for i in n_loops:
        threads.append(threading.Thread(target=loop, args=(i, loops[i])))
    for j in n_loops:
        threads[j].start()

    for k in n_loops:
        # join(self, timeout=None)方法等待所有线程结束，也可以提供超时时间
        # 超过timeout时间会跳到主线程。这里使用的是threading模块，即使跳到主线程
        # 也会等待子线程结束程序才结束。
        # threads[k].join(timeout=3)
        threads[k].join()
    print('All done at:', ctime())


if __name__ == '__main__':
    main()
