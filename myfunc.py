def myfunc(*args):
    for a in args:
        print(a, end='   ')
    if args:
        print()

def nyfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k,v,sep='->', end='  ')
    if kwargs:
        print()

