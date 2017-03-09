#!/usr/bin/python3

t = int(input())
for _ in range(t):
    n,c,m = map(int, input().split())
    chocs = n // c
    w = chocs 
    while w >=m:
        chocs += w // m
        w = w // m + w % m

    print(chocs)
        
