#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Thread, Lock, currentThread
from time import ctime, sleep
from atexit import register
import random

lock = Lock()
loops = (random.randrange(2, 5) for x in range(random.randrange(3, 7)))

remaining = set()


def loop(sleep_time):
    # 第一种：使用acquire()获得锁，使用release()释放锁。
    thread_name = currentThread().name
    lock.acquire()
    remaining.add(thread_name)
    print('[%s] Started %s' % (ctime(), thread_name))
    lock.release()

    sleep(sleep_time)

    lock.acquire()
    remaining.remove(thread_name)
    print('[%s] Completed %s(%d secs)' % (ctime(), thread_name, sleep_time))
    print('(remaining: %s)' % (remaining or 'None'))
    lock.release()


def loop_use_context(sleep_time):
    # 第二种：上下文管理器
    # 每个对象的上下文管理器负责在进入该套件之前调用acquire()并在完成执行之后调用release()
    thread_name = currentThread().name
    with lock:
        remaining.add(thread_name)
        print('[%s] Started %s' % (ctime(), thread_name))

    sleep(sleep_time)

    with lock:
        remaining.remove(thread_name)
        print('[%s] Completed %s(%d secs)' % (ctime(), thread_name, sleep_time))
        print('(remaining: %s)' % (remaining or 'None'))


def main():
    # 同步原语之锁
    for sleep_time in loops:
        Thread(target=loop_use_context, args=(sleep_time,)).start()


@register
def at_exit():
    print('All done at:', ctime())


if __name__ == '__main__':
    main()
