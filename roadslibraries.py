#!/usr/bin/python3

q = int(input())
for i in range(q):
    n,m,libCost,roadCost = map(int, input().split())
    for _ in range(m):
        _ = input()
        
    if libCost < roadCost:
        print(n*libCost)
    else:
        if n > m:
            libCount = n - m
            roadCount = m
        else:
            libCount = 1
            roadCount = n - 1
                
        print(libCount * libCost + roadCount * roadCost)
