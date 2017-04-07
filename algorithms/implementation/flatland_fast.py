#!/usr/bin/python3

n,m = map(int, input().split())
c = sorted(map(int,input().split()))

maximum = max(c[0], n - c[-1] - 1) 
for i in range(1, m):
    d = c[i] - c[i-1]
    maximum = max(d//2, maximum)
print(maximum)
