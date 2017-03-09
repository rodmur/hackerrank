#!/usr/bin/python3

import sys

a = list(map(int, input().split()))
asum = minsum = maxsum = 0

for i in range(len(a)):
    tmpa = list(a)
    __ = tmpa.pop(i)
    asum = sum(tmpa)
    if asum > maxsum: 
        maxsum = asum
    if i == 0 or asum < minsum:
        minsum = asum
    del tmpa

print(minsum, maxsum)

