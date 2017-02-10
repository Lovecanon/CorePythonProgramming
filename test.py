from atexit import register
import os


@register
def at_exit():
    print('register executed!')

if __name__ == '__main__':
    print('start')
    # os._exit(0)
    print('end')