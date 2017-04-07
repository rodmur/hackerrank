#!/usr/bin/python3
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    inv = 0
    for i in range(N):
        for j in range(i+1,N):
            if A[i] > A[j]: 
                inv += 1
    if inv & 1 == 0:
        print("YES")
    else:
        print("NO")
