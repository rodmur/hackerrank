#!/usr/bin/python3

import sys
from math import sqrt

T = int(input())

maxn = 0
possp = []

for i in range(T):
    n = int(input())
    possp.append(n)
    if n > maxn:
        maxn = n

maxn += 2
A = [True] * maxn

for i in range(2,int(sqrt(maxn))):
    k = 0
    j = i**2
    while j < maxn:
        A[j] = False
        k += 1
        j = i**2+k*i

for k in possp:
    if A[k]:
        print("Prime:", k)
    else:
        print("Not prime:", k)
    
