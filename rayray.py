#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    rt = [0 for _ in range(n)]

    for qsa in queries:
        if qsa[0] - 1 >= 0:
            rt[qsa[0] - 1] += qsa[2]
        if qsa[1] < n:
            rt[qsa[1]] -= qsa[2]

    beet = 0
    maxy = 0
    for i in range(n):
        beet += rt[i]
        maxy = max(maxy, beet)

    return maxy

def gen(fp):
    for i in range(100000):
        yield [int(x) for x in fp.readline().split(" ")]

if __name__ == '__main__':

    fp = open("input07.txt")
    fp.readline()
    result = arrayManipulation(10000000, gen(fp))

    print(result)
