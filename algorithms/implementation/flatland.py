#!/usr/bin/python3

import sys

n,m = map(int, input().split())

if n == m:
    print(0)
    sys.exit(0)

c = sorted(map(int,input().split()))

left = right = False

if c[0] != 0:
    c.insert(0,0)
    left = True

if c[-1] != n-1:
    c.append(n-1)
    right = True

dists = []
for i in range(1,len(c)):
    if (i == 1 and left) or (i == len(c) - 1 and right):
        d = abs(c[i-1] - c[i]) 
    else:
        d = abs(c[i-1] - c[i]) // 2
    dists.append(d)

print(max(dists))
    
