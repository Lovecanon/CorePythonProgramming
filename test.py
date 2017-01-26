
def tesy(*args):
    print('*args:', *args)
    print('args:', args)
    for a in args:
        print(a)

tesy('111', '2222')