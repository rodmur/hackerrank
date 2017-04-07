#!/usr/bin/python3

n,m = map(int, input())
C = list(map(int, input().split()))

high = max(C)
counts = [[ 0 for x in range(high+1) ] for y in range(n+1)]

for i in range(n+1):
    for j in range(high+1):
        
