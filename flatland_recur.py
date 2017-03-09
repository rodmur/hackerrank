#!/usr/bin/python3

def find_dist(v, A):
# assumes A is sorted, chop it in halves until we find what we want
    dist = 0
    if len(A) >= 2:
        y = len(A)//2
        L = A[:y]
        R = A[y:]
        if v <= L[-1] or abs(L[-1]-v) < abs(R[0]-v):
            dist = find_dist(v, L)
        else:
            dist = find_dist(v, R)
    else:
        if len(A) == 0:
            dist = 0
        elif len(A) == 1:
            dist = abs(A[0] - v)
        else:
            dist = min(abs(A[0]-v),abs(A[1]-v)) 
    return dist
        

n,m = map(int, input().split())
c = sorted(map(int,input().split()))

dist = []
for x in range(n):
    d = find_dist(x, c)
    dist.append(d)

print(max(dist))
