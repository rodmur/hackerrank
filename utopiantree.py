#!/usr/bin/python3

import sys


n = int(sys.argv[1])

h = 0

for i in range(n+1):
    if i & 1:
        h *= 2
    else:
        h += 1

print(h)

