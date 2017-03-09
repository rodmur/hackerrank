#!/usr/bin/python3

import sys
from statistics import mode,StatisticsError

n = int(input())
a = list(map(int, input().split()))

def nomode(a):
    b = {}
    for i in a:
        b[i] = a.count(i)
        
    val = max(b, key=lambda x: b[x])
    return b[val] 

try:
    val = mode(a)
    cnt = a.count(val)
except StatisticsError:
    cnt = nomode(a)
    
print(n - cnt)

