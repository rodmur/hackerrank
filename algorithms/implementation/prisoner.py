#!/usr/bin/python3

T = int(input())
for _ in range(T):
    n,m,s = map(int, input().split())
    if n > 1: 
        result = (m+s-1) % n  
    else: 
        result = 1
    if result == 0:
        result = n
    print(result)

