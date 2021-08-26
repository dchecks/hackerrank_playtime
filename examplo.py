class Examplo:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def funny_func(a):
    b = 2
    if a < b:
        print("Todo veces")


def otra_funncy_func(c):
    a = 1
    b = 2
    if (a+c) > (b+c):
        print("Todo veces?")


def otra_func():
    if (True or False) and (True and True):
        print("Todo amor")


def add_puro(a, b):
    return a + b



e = Examplo(5, 10)
pf_val = add_puro(e.a, e.b)

print(pf_val)


