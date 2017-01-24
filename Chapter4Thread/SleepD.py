#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
from time import ctime, sleep

loops = (4, 2)


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)


def loop(n_loop, sleep_time):
    print('start loop', n_loop, ' at:', ctime())
    sleep(sleep_time)
    print('end loop', n_loop, ' at:', ctime())


def main():
    # 创建Thread的实例之派生Thread的子类，并创建子类的实例
    print('Starting at:', ctime())
    n_loops = range(len(loops))
    threads = []
    for i in n_loops:
        threads.append(MyThread(loop, (i, loops[i])))
    for j in n_loops:
        threads[j].start()
    for k in n_loops:
        threads[k].join()
    print('All done at:', ctime())

if __name__ == '__main__':
    main()