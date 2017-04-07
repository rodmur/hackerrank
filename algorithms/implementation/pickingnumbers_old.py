#!/usr/bin/python3

n = int(input())
a = list(map(int, input().split()))
seta = set(a)

amax = 2
for k in seta:
    newt = list(filter(lambda x: abs(x - k) <= 1, a))
    d = len(newt)
    if d > amax:
        amax = d
        new = newt

low = min(new)
high = max(new)

lower = []
upper = []
for i in range(len(new)):
    if abs(new[i] - low) <= 1:
        lower.append(new[i])
    if abs(new[i] - high) <= 1:
        upper.append(new[i])

m = len(upper)
l = len(lower)

if m == l:
    print(m+1)
else:
    print(max(m,l))
