#!/usr/bin/python3

n,m = map(int, input().split())
c = sorted(map(int,input().split()))

dist = []
for x in range(n):
    A = list(c)
    while len(A) >= 2:
        y = len(A)//2
        L = A[:y]
        R = A[y:]
        if x <= L[-1] or abs(L[-1]-x) < abs(R[0]-x):
            A = L
        else:
            A = R

        if len(A) == 0:
            d = 0
            dist.append(d)
        if len(A) == 1:
            d = abs(A[0] - x)
            dist.append(d)
        if len(A) == 2:
            d = min(abs(A[0]-x),abs(A[1]-x)) 
            dist.append(d)

print(max(dist))
