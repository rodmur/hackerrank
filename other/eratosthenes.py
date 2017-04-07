#!/usr/bin/python3

import sys
from math import sqrt

n = int(input())

A = [True] * n

for i in range(2,int(sqrt(n))):
    if A[i]:
        k = 0
        j = i**2
        while j < n:
            A[j] = False
            k += 1
            j = i**2+k*i

for i in range(n):
    if A[i]:
        print(i,end=' ')

print()
    
