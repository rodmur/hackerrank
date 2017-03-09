#!/usr/bin/python3

n,k = map(int, input().split())
S = list(map(int, input().split()))

Q = [0]*k

for i in S:
    Q[i % k] += 1
res = 0
for i in range(k//2+1):
    if i ==0 or k == i*2:
        res += 1 if Q[i] > 0 else 0
    else:
        res += max(Q[i], Q[k-i])

print(res)
