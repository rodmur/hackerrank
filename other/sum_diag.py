#!/usr/bin/python3

import sys

n = int(input())

a = []

for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().split()]
    a.append(a_t)

lsum = rsum = 0

for i in range(n):
    lsum += a[i][i]
    rsum += a[i][n-1-i]

print(abs(lsum-rsum))
