#!/usr/bin/python3

t = int(input())
for _ in range(t):
    n,c,m = map(int, input().split())
    print(n//c+(n//c-1)//(m-1))

