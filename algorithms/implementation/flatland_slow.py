#!/usr/bin/python3

n,m = map(int, input().split())
c = sorted(map(int,input().split()))

dist = []
d = 0
for x in range(n):
    if x in c:
        d = 0
    else:
        for i in range(m-1):
            if x < c[0]:
                d = abs(c[0]-x) 
            if x > c[-1]:
                d = abs(c[-1]-x) 
            if c[i] <= x <= c[i+1]:
                d = min(abs(c[i]-x),abs(c[i+1]-x)) 
                
    dist.append(d)

print(max(dist))
