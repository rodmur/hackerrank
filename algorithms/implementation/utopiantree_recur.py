#!/usr/bin/python3

import sys

def grow(n):
    growth = 0
    if n == 0:
        return 1
    elif n & 1:
        growth = 2*(grow(n-1))
    else:
        growth = grow(n-1) + 1

    return growth


n = int(sys.argv[1])

h = grow(n)
print(h)

