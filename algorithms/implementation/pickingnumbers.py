#!/usr/bin/python3

n = int(input())
a = list(map(int, input().split()))

maxn = 0
for x in a:
    temp = a.count(x) + a.count(x+1)
    if temp > maxn:
        maxn = temp
print(maxn)
