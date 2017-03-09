#!/usr/bin/python3

T = int(input().strip())
for _ in range(T):
    n , k = map(int , input().split())
    if ((k-1) | k) <= n:
        print(k-1)
    else:
        print(k-2)
