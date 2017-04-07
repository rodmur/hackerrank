#!/usr/bin/python3

import sys

n,k,q = map(int, input().split())
a = list(map(int, input().split()))

k %= n
rota = a[-k:] + a[:-k]

for _ in range(q):
    m = int(input().strip())
    print(rota[m])

