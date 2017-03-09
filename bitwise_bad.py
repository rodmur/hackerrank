#!/usr/bin/python3

import sys

t = int(input().strip())

for a0 in range(t):
    n,k = [ int(x) for x in input().split() ]
    maxv = 0
    for a in range(1,n):
        for b in range(2,n+1):
            t = a & b
            if t > maxv and t < k:
                maxv = t
    print(maxv)

