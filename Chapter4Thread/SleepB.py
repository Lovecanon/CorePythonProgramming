#!/usr/bin/env python
# -*- coding: utf-8 -*-
import _thread
from time import ctime, sleep

loops = [4, 2]


def loop(n_loop, sleep_time, lock):
    print('start loop ', n_loop, ' at:', ctime())
    sleep(sleep_time)
    print('end loop ', n_loop, ' at:', ctime())
    lock.release()


def main():
    # 和SleepA相比，不使用主线程等待—sleep(6)，而是使用while循环+判断是否被lock
    # 直到所有的锁都被释放，才终止while循环
    print('Starting at:', ctime())
    locks = []
    n_loops = range(len(loops))
    for _ in n_loops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in n_loops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in n_loops:
        # locked() 如果锁对象没有释放返回True，锁对象已经释放返回False
        # 下面会一直while循环，直到所有的锁被释放才跳过while循环执行下面打印语句
        while locks[i].locked():
            pass
    print('All done at:', ctime())

if __name__ == '__main__':
    main()





