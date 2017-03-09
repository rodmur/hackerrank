#!/usr/bin/python3

import sys
from math import gcd
from functools import reduce

def lcm(a,b):
    return (a * b) // gcd(a,b)

n,m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

lcmval = reduce(lcm, A)
gcdval = reduce(gcd, B)

lcmtemp = lcmval

count = 0
while lcmval <= gcdval: 
    if (gcdval % lcmval) == 0:
        count += 1
    lcmval += lcmtemp

print(count)
