import itertools

import numpy as np


def gen():
    i = 1
    while 1:
        dnp = np.fmod([i], [99, 108, 111, 115, 101])
        if not all(dnp):
            yield i
        else:
            i += 1


def g2():
    for i in itertools.count(start=1):  print("blah")

eggs = (i for i in itertools.count(start=1) if not all(np.fmod([i], [99, 108, 111, 115, 101])))

# gen()
# g2()
while 1:
    print(eggs.__next__())